import time
import requests
from django.core.management.base import BaseCommand
from django.db import transaction
from analysis.models import Company, FinancialDocument
from datetime import datetime

# Alpha Vantage API Key
ALPHA_VANTAGE_API_KEY = '3D3KDQX0TSLTSDO4'      #'F3Z55WYNQY3KJ1Y0'  # Replace with your API key   'WAE0T1ELGUKW2DC0'
NUM_YEARS = 10  # Define the number of years to process
GLOBAL_DELAY = 15  # Global delay in seconds between API requests


def fetch_financial_data(symbol, report_type):
    """
    Fetch financial data for a given symbol and report type from Alpha Vantage.
    """
    url = f'https://www.alphavantage.co/query?function={report_type}&symbol={symbol}&apikey={ALPHA_VANTAGE_API_KEY}'
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        # Check for rate limit errors
        if "Note" in data:
            print(f"Rate limit hit for {symbol}: {data['Note']}")
            time.sleep(60)  # Wait for a minute before retrying
            return None

        # Handle specific data structures
        if report_type in ['INCOME_STATEMENT', 'BALANCE_SHEET', 'CASH_FLOW']:
            if 'annualReports' not in data:
                print(f"No annual reports data found for {symbol} ({report_type}).")
                return None

            # Filter reports for the last NUM_YEARS
            current_year = datetime.now().year
            annual_reports = [
                report for report in data['annualReports']
                if current_year - int(report['fiscalDateEnding'][:4]) < NUM_YEARS
            ]
            return annual_reports
        elif report_type == 'OVERVIEW':
            if 'SharesOutstanding' not in data:
                print(f"No SharesOutstanding data found for {symbol} in overview.")
                return None
            return data

        return None
    except requests.exceptions.RequestException as e:
        print(f"Network error fetching data for {symbol}: {e}")
        return None
    except KeyError as e:
        print(f"KeyError: Missing key {e} in response for {symbol} ({report_type}).")
        return None
    finally:
        print(f"Finished processing request for {symbol} ({report_type}).")


class Command(BaseCommand):
    help = 'Fetch financial data from Alpha Vantage API and update the database'

    def handle(self, *args, **kwargs):
        companies = Company.objects.all()

        for company in companies:
            print(f"Fetching data for {company.symbol}...")

            # Fetch different types of financial data
            income_statements = fetch_financial_data(company.symbol, 'INCOME_STATEMENT')
            balance_sheets = fetch_financial_data(company.symbol, 'BALANCE_SHEET')
            cash_flows = fetch_financial_data(company.symbol, 'CASH_FLOW')
            company_overview = fetch_financial_data(company.symbol, 'OVERVIEW')

            # Check for missing data
            if not income_statements or not balance_sheets or not cash_flows:
                print(f"Skipping {company.symbol} due to missing financial reports.")
                continue

            if not company_overview:
                print(f"Skipping {company.symbol} due to missing company overview data.")
                continue

            # Process and save data
            try:
                with transaction.atomic():
                    for report in income_statements:
                        year = int(report['fiscalDateEnding'][:4])
                        income_statement = report
                        balance_sheet = next(
                            (bs for bs in balance_sheets if int(bs['fiscalDateEnding'][:4]) == year), {}
                        )
                        cash_flow = next(
                            (cf for cf in cash_flows if int(cf['fiscalDateEnding'][:4]) == year), {}
                        )

                        # Update or create FinancialDocument records
                        FinancialDocument.objects.update_or_create(
                            company=company,
                            year=year,
                            defaults={
                                'revenue': income_statement.get('totalRevenue'),
                                'net_income': income_statement.get('netIncome'),
                                'operating_expenses': income_statement.get('operatingExpenses'),
                                'r_and_d_costs': income_statement.get('researchAndDevelopment'),
                                'shares_outstanding': company_overview.get('SharesOutstanding', None),
                                'cogs': income_statement.get('costofGoodsAndServicesSold'),
                                'gross_profit': income_statement.get('grossProfit'),
                                'total_assets': balance_sheet.get('totalAssets'),
                                'current_assets': balance_sheet.get('totalCurrentAssets'),
                                'current_liabilities': balance_sheet.get('totalCurrentLiabilities'),
                                'cash_and_cash_equivalents': balance_sheet.get('cashAndCashEquivalentsAtCarryingValue'),
                                'total_liabilities': balance_sheet.get('totalLiabilities'),
                                'shareholders_equity': balance_sheet.get('totalShareholderEquity'),
                                'operating_cash_flow': cash_flow.get('operatingCashflow'),
                                'capital_expenditures': cash_flow.get('capitalExpenditures'),
                            }
                        )
                        print(f"Updated financial data for {company.symbol}, Year: {year}.")
            except Exception as e:
                print(f"Error saving data for {company.symbol}: {e}")

            # Delay to avoid hitting the API rate limit
            time.sleep(GLOBAL_DELAY)  # Global delay between requests

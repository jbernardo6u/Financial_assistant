# analysis/management/commands/fetch_financial_data.py

import time
import requests
from django.core.management.base import BaseCommand
from analysis.models import Company, FinancialDocument

ALPHA_VANTAGE_API_KEY = 'WAE0T1ELGUKW2DC0'
NUM_YEARS = 5  # Define the number of years to process

def fetch_financial_data(symbol, report_type):
    url = f'https://www.alphavantage.co/query?function={report_type}&symbol={symbol}&apikey={ALPHA_VANTAGE_API_KEY}'
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        # Debug: Print the full response
        print(f"Response for {symbol} ({report_type}): {data}")

        # Check for rate limit errors
        if "Note" in data:
            print(f"Rate limit hit for symbol {symbol}: {data['Note']}")
            time.sleep(60)  # Wait for a minute before retrying
            return None

        # Check for the expected data structure
        if 'annualReports' not in data:
            print(f"No annual reports data found for symbol {symbol}.")
            return None

        return data['annualReports'][-NUM_YEARS:]  # Limit to the last NUM_YEARS reports
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data for {symbol}: {e}")
        return None

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

            # Check for rate limits or missing data
            if not income_statements and not balance_sheets and not cash_flows:
                print(f"Skipping {company.symbol} due to missing data.")
                continue

            if not company_overview:
                print(f"Company overview data is missing for {company.symbol}. Skipping...")
                continue

            for i, report in enumerate(income_statements or []):
                try:
                    year = int(report['fiscalDateEnding'][:4])
                    income_statement = report
                    balance_sheet = balance_sheets[i] if i < len(balance_sheets) else {}
                    cash_flow = cash_flows[i] if i < len(cash_flows) else {}

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
                            'grossProfit': income_statement.get('grossProfit'),
                            'total_assets': balance_sheet.get('totalAssets'),
                            'current_assets': balance_sheet.get('currentAssets'),
                            'current_liabilities': balance_sheet.get('currentLiabilities'),
                            'cash_and_cash_equivalents': balance_sheet.get('cashAndCashEquivalentsAtCarryingValue'),
                            'total_liabilities': balance_sheet.get('totalLiabilities'),
                            'shareholders_equity': balance_sheet.get('totalShareholderEquity'),
                            'operating_cash_flow': cash_flow.get('operatingCashflow'),
                            'capital_expenditures': cash_flow.get('capitalExpenditures')
                        }
                    )
                    print(f"Updated financial data for {company.symbol}, {year}.")
                except KeyError as e:
                    print(f"Missing data for {company.symbol} in year {year}: {e}")

            # Delay to avoid hitting the API rate limit
            time.sleep(12)  # Adjust as needed


# analysis/management/commands/fetch_financial_repport.py

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

            if not income_statements or not balance_sheets or not cash_flows:
                print(f"Skipping {company.symbol} due to missing data.")
                continue

            for i, report in enumerate(income_statements):
                try:
                    year = int(report['fiscalDateEnding'][:4])

                    # Find corresponding data in the other reports for the same year
                    balance_sheet = balance_sheets[i]
                    cash_flow = cash_flows[i]

                    FinancialDocument.objects.update_or_create(
                        company=company,
                        year=year,
                        defaults={
                            'revenue': report.get('totalRevenue'),
                            'net_income': report.get('netIncome'),
                            'total_assets': balance_sheet.get('totalAssets'),
                            'total_liabilities': balance_sheet.get('totalLiabilities'),
                            'operating_cash_flow': cash_flow.get('operatingCashflow'),
                            'capital_expenditures': cash_flow.get('capitalExpenditures')
                        }
                    )
                    print(f"Updated financial data for {company.symbol}, {year}.")
                except KeyError as e:
                    print(f"Missing data for {company.symbol} in year {year}: {e}")

            # Delay to avoid hitting the API rate limit
            time.sleep(12)  # Adjust as needed

# analysis/management/commands/fetch_financial_data.py

import time
import requests
from django.core.management.base import BaseCommand
from analysis.models import Company, FinancialDocument

ALPHA_VANTAGE_API_KEY = 'WAE0T1ELGUKW2DC0'


def fetch_financial_data(symbol):
    url = f'https://www.alphavantage.co/query?function=INCOME_STATEMENT&symbol={symbol}&apikey={ALPHA_VANTAGE_API_KEY}'
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raises an error for HTTP errors
        data = response.json()

        # Check for expected data structure
        if 'annualReports' not in data:
            print(f"No annual reports data found for symbol {symbol}.")
            return None

        return data
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data for {symbol}: {e}")
        return None


class Command(BaseCommand):
    help = 'Fetch financial data from Alpha Vantage API and update the database'

    def handle(self, *args, **kwargs):
        companies = Company.objects.all()
        for company in companies:
            print(f"Fetching data for {company.symbol}...")
            data = fetch_financial_data(company.symbol)

            # Skip if no data returned
            if not data:
                continue

            for report in data['annualReports']:
                try:
                    year = int(report['fiscalDateEnding'][:4])
                    FinancialDocument.objects.update_or_create(
                        company=company,
                        year=year,
                        defaults={
                            'revenue': report.get('totalRevenue'),
                            'net_income': report.get('netIncome'),
                            'total_assets': report.get('totalAssets'),
                            'total_liabilities': report.get('totalLiabilities'),
                            'operating_cash_flow': report.get('operatingCashflow'),
                            'capital_expenditures': report.get('capitalExpenditures')
                        }
                    )
                    print(f"Updated financial data for {company.symbol}, {year}.")
                except KeyError as e:
                    print(f"Missing expected data for {company.symbol} in year {year}: {e}")

            # To avoid hitting the API rate limit, add a short delay
            time.sleep(12)  # Adjust based on Alpha Vantage rate limit

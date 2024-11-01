from django.core.management.base import BaseCommand
from analysis.models import Company, FinancialDocument
import requests

ALPHA_VANTAGE_API_KEY = 'WAE0T1ELGUKW2DC0'
def fetch_financial_data(symbol):
    url = f'https://www.alphavantage.co/query?function=INCOME_STATEMENT&symbol={symbol}&apikey={ALPHA_VANTAGE_API_KEY}'
    response = requests.get(url)
    return response.json()


class Command(BaseCommand):
    help = 'Fetch financial data from Alpha Vantage API'

    def handle(self, *args, **kwargs):
        companies = Company.objects.all()
        for company in companies:
            data = fetch_financial_data(company.symbol)
            for report in data['annualReports']:
                report_year = int(report['fiscalDateEnding'][:4])
                FinancialDocument.objects.update_or_create(
                    company=company,
                    report_year=report_year,
                    defaults={
                        'revenue': report['totalRevenue'],
                        'net_income': report['netIncome'],
                        'total_assets': report['totalAssets'],
                        'total_liabilities': report['totalLiabilities'],
                        'operating_cash_flow': report['operatingCashflow'],
                        'capital_expenditures': report['capitalExpenditures']
                    }
                )

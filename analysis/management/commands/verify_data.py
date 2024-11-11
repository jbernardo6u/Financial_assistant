# analysis/management/commands/verify_data.py

from django.core.management.base import BaseCommand
from analysis.models import Company, FinancialDocument, FinancialIndicator


class Command(BaseCommand):
    help = 'Verify all financial data is saved in the database'

    def handle(self, *args, **kwargs):
        companies = Company.objects.all()
        for company in companies:
            financial_docs = FinancialDocument.objects.filter(company=company).count()
            financial_indicators = FinancialIndicator.objects.filter(company=company).count()

            print(f"Company: {company.name} ({company.symbol})")
            print(f"  Financial Documents: {financial_docs}")
            print(f"  Financial Indicators: {financial_indicators}")

            # Additional checks for specific data or fields
            incomplete_docs = FinancialDocument.objects.filter(
                company=company,
                revenue__isnull=True
            )
            if incomplete_docs.exists():
                print(f"  Incomplete Financial Documents for {company.symbol}:")
                for doc in incomplete_docs:
                    print(f"    - Year: {doc.year}")

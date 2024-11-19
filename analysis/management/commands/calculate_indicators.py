from django.core.management.base import BaseCommand
from django.db import transaction
from analysis.models import Company, FinancialDocument, FinancialIndicator
from decimal import Decimal


class Command(BaseCommand):
    help = 'Calculate financial indicators based on financial documents'

    def calculate_profitability_indicators(self, doc, previous_doc=None):
        revenue = Decimal(doc.revenue or 0)
        cogs = Decimal(doc.cogs or 0)  # Cost of Goods Sold
        operating_expenses = Decimal(doc.operating_expenses or 0)
        r_and_d_costs = Decimal(doc.r_and_d_costs or 0)
        net_income = Decimal(doc.net_income or 0)
        shares_outstanding = Decimal(doc.shares_outstanding or 0)

        # Gross Profit and Gross Profit Margin
        gross_profit = revenue - cogs
        gross_profit_margin = (gross_profit / revenue) if revenue else None

        # Operating Profit and Operating Profit Margin
        operating_profit = gross_profit - operating_expenses - r_and_d_costs
        operating_profit_margin = (operating_profit / gross_profit) if gross_profit else None

        # Net Profit Margin
        net_profit_margin = (net_income / revenue) if revenue else None

        # Earnings Per Share (EPS)
        eps = (net_income / shares_outstanding) if shares_outstanding else None

        # Profit Growth Rate
        profit_growth_rate = None
        if previous_doc:
            previous_net_income = Decimal(previous_doc.net_income or 0)
            if previous_net_income:
                profit_growth_rate = (net_income - previous_net_income) / previous_net_income

        return {
            'gross_profit_margin': gross_profit_margin,
            'operating_profit_margin': operating_profit_margin,
            'net_profit_margin': net_profit_margin,
            'earnings_per_share': eps,
            'profit_growth_rate': profit_growth_rate,
        }

    def calculate_balance_sheet_indicators(self, doc):
        total_liabilities = Decimal(doc.total_liabilities or 0)
        shareholders_equity = Decimal(doc.shareholders_equity or 0)
        current_assets = Decimal(doc.current_assets or 0)
        current_liabilities = Decimal(doc.current_liabilities or 0)
        cash_and_cash_equivalents = Decimal(doc.cash_and_cash_equivalents or 0)
        total_assets = Decimal(doc.total_assets or 0)

        # Debt Ratio
        debt_ratio = (total_liabilities / shareholders_equity) if shareholders_equity else None

        # Current Ratio
        current_ratio = (current_assets / current_liabilities) if current_liabilities else None

        # Cash Ratio
        cash_ratio = (cash_and_cash_equivalents / total_assets) if total_assets else None

        return {
            'debt_ratio': debt_ratio,
            'current_ratio': current_ratio,
            'cash_ratio': cash_ratio,
        }

    def calculate_cash_flow_indicators(self, doc):
        operating_cash_flow = Decimal(doc.operating_cash_flow or 0)
        capital_expenditures = Decimal(doc.capital_expenditures or 0)

        # Free Cash Flow
        free_cash_flow = operating_cash_flow - capital_expenditures

        # Capital Expenditure Ratio
        capital_expenditure_ratio = (capital_expenditures / operating_cash_flow) if operating_cash_flow else None

        return {
            'operating_cash_flow': operating_cash_flow,
            'free_cash_flow': free_cash_flow,
            'capital_expenditure_ratio': capital_expenditure_ratio,
        }

    def handle(self, *args, **kwargs):
        companies = Company.objects.all()

        for company in companies:
            financial_docs = FinancialDocument.objects.filter(company=company).order_by('year')

            previous_doc = None
            for doc in financial_docs:
                # Calculate indicators
                profitability_indicators = self.calculate_profitability_indicators(doc, previous_doc)
                balance_sheet_indicators = self.calculate_balance_sheet_indicators(doc)
                cash_flow_indicators = self.calculate_cash_flow_indicators(doc)

                # Combine all indicators
                indicators = {**profitability_indicators, **balance_sheet_indicators, **cash_flow_indicators}

                # Add the report year from FinancialDocument to indicators
                indicators['year'] = doc.year

                # Create or update FinancialIndicator record
                with transaction.atomic():
                    FinancialIndicator.objects.update_or_create(
                        company=company,
                        document=doc,
                        defaults=indicators
                    )

                print(f"Calculated indicators for {company.symbol}, year {doc.year}")

                # Update the previous document for the next iteration
                previous_doc = doc

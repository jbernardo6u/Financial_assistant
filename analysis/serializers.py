from rest_framework import serializers
from analysis.models import Company, FinancialDocument, FinancialIndicator

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['id', 'symbol', 'name']

class FinancialDocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = FinancialDocument
        fields = ['year', 'revenue', 'net_income', 'operating_expenses', 'r_and_d_costs', 'shares_outstanding', 'cogs',
                  'gross_profit', 'total_assets', 'current_assets', 'current_liabilities', 'cash_and_cash_equivalents',
                  'total_liabilities', 'shareholders_equity', 'operating_cash_flow',
                  'capital_expenditures']

class FinancialIndicatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = FinancialIndicator
        fields = ['year', 'gross_profit_margin', 'net_profit_margin', 'profit_growth_rate', 'earnings_per_share',
                  'debt_ratio', 'current_ratio', 'cash_ratio', 'operating_cash_flow',  'free_cash_flow',
                  'capital_expenditure_ratio']


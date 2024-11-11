from rest_framework import serializers
from analysis.models import Company, FinancialDocument, FinancialIndicator

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['id', 'symbol', 'name']

class FinancialDocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = FinancialDocument
        fields = ['report_year', 'revenue', 'net_income', 'total_assets', 'total_liabilities', 'operating_cash_flow', 'capital_expenditures']

class FinancialIndicatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = FinancialIndicator
        fields = ['report_year', 'gross_profit_margin', 'net_profit_margin', 'debt_ratio', 'free_cash_flow']

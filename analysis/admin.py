# analysis/admin.py
from django.contrib import admin
from .models import FinancialIndicator, FinancialDocument
# Register your models here.

@admin.register(FinancialDocument)
class FinancialDocumentAdmin(admin.ModelAdmin):
    list_display = ('year', 'revenue', 'net_income', 'operating_expenses', 'r_and_d_costs', 'shares_outstanding',
                    'cogs', 'gross_profit', 'total_assets', 'current_assets', 'current_liabilities',
                    'cash_and_cash_equivalents', 'total_liabilities', 'shareholders_equity', 'operating_cash_flow',
                  'capital_expenditures')

@admin.register(FinancialIndicator)
class FinancialIndicatorAdmin(admin.ModelAdmin):
    list_display = ('company', 'year', 'document', 'gross_profit_margin', 'net_profit_margin', 'profit_growth_rate',
                    'earnings_per_share', 'debt_ratio', 'current_ratio', 'cash_ratio', 'operating_cash_flow',
                    'free_cash_flow',
                  'capital_expenditure_ratio')


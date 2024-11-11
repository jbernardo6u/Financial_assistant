from django.utils import timezone
from django.db import models

# Create your models here.

class Company(models.Model):
    symbol = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class FinancialDocument(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    year = models.IntegerField()

    revenue = models.BigIntegerField(null=True, blank=True)
    net_income = models.BigIntegerField(null=True, blank=True)
    # Add the cogs (Cost of Goods Sold) field if it's missing
    operating_expenses = models.BigIntegerField(null=True, blank=True)
    r_and_d_costs = models.BigIntegerField(null=True, blank=True)
    shares_outstanding = models.BigIntegerField(null=True, blank=True)
    cogs = models.BigIntegerField(null=True, blank=True)  # Cost of Goods Sold
    gross_profit = models.BigIntegerField(null=True, blank=True)

    total_assets = models.BigIntegerField(null=True, blank=True)
    current_assets = models.BigIntegerField(null=True, blank=True)
    current_liabilities = models.BigIntegerField(null=True, blank=True)
    cash_and_cash_equivalents = models.BigIntegerField(null=True, blank=True)
    total_liabilities = models.BigIntegerField(null=True, blank=True)
    shareholders_equity = models.BigIntegerField(null=True, blank=True)

    operating_cash_flow = models.BigIntegerField(null=True, blank=True)
    capital_expenditures = models.BigIntegerField(null=True, blank=True)


    class Meta:
        unique_together = ('company', 'year')


class FinancialIndicator(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    year = models.IntegerField()
    document = models.ForeignKey(FinancialDocument, on_delete=models.CASCADE)


    # Profitability Indicators
    gross_profit_margin = models.DecimalField(max_digits=10, decimal_places=4, null=True, blank=True)
    operating_profit_margin = models.DecimalField(max_digits=10, decimal_places=4, null=True, blank=True)
    net_profit_margin = models.DecimalField(max_digits=10, decimal_places=4, null=True, blank=True)
    profit_growth_rate = models.DecimalField(max_digits=10, decimal_places=4, null=True, blank=True)
    earnings_per_share = models.DecimalField(max_digits=10, decimal_places=4, null=True, blank=True)

    # Balance Sheet Indicators
    debt_ratio = models.DecimalField(max_digits=10, decimal_places=4, null=True, blank=True)
    current_ratio = models.DecimalField(max_digits=10, decimal_places=4, null=True, blank=True)
    cash_ratio = models.DecimalField(max_digits=10, decimal_places=4, null=True, blank=True)

    # Cash Flow Indicators
    operating_cash_flow = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    free_cash_flow = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    capital_expenditure_ratio = models.DecimalField(max_digits=10, decimal_places=4, null=True, blank=True)

    # other fields...
    calculated_at = models.DateTimeField(default=timezone.now)

    class Meta:
        unique_together = ('company', 'year')
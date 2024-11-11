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
    total_assets = models.BigIntegerField(null=True, blank=True)
    total_liabilities = models.BigIntegerField(null=True, blank=True)
    operating_cash_flow = models.BigIntegerField(null=True, blank=True)
    capital_expenditures = models.BigIntegerField(null=True, blank=True)
    class Meta:
        unique_together = ('company', 'year')

class FinancialIndicator(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    year = models.IntegerField()
    gross_profit_margin = models.FloatField()
    net_profit_margin = models.FloatField()
    debt_ratio = models.FloatField()
    free_cash_flow = models.BigIntegerField()

    class Meta:
        unique_together = ('company', 'year')

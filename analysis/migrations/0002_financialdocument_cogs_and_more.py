# Generated by Django 5.1.2 on 2024-11-11 22:07

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("analysis", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="financialdocument",
            name="cogs",
            field=models.BigIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="financialindicator",
            name="calculated_at",
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name="financialindicator",
            name="capital_expenditure_ratio",
            field=models.DecimalField(
                blank=True, decimal_places=4, max_digits=10, null=True
            ),
        ),
        migrations.AddField(
            model_name="financialindicator",
            name="cash_ratio",
            field=models.DecimalField(
                blank=True, decimal_places=4, max_digits=10, null=True
            ),
        ),
        migrations.AddField(
            model_name="financialindicator",
            name="current_ratio",
            field=models.DecimalField(
                blank=True, decimal_places=4, max_digits=10, null=True
            ),
        ),
        migrations.AddField(
            model_name="financialindicator",
            name="document",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="analysis.financialdocument",
            ),
        ),
        migrations.AddField(
            model_name="financialindicator",
            name="earnings_per_share",
            field=models.DecimalField(
                blank=True, decimal_places=4, max_digits=10, null=True
            ),
        ),
        migrations.AddField(
            model_name="financialindicator",
            name="operating_cash_flow",
            field=models.DecimalField(
                blank=True, decimal_places=2, max_digits=15, null=True
            ),
        ),
        migrations.AddField(
            model_name="financialindicator",
            name="operating_profit_margin",
            field=models.DecimalField(
                blank=True, decimal_places=4, max_digits=10, null=True
            ),
        ),
        migrations.AddField(
            model_name="financialindicator",
            name="profit_growth_rate",
            field=models.DecimalField(
                blank=True, decimal_places=4, max_digits=10, null=True
            ),
        ),
        migrations.AlterField(
            model_name="financialdocument",
            name="capital_expenditures",
            field=models.BigIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="financialdocument",
            name="net_income",
            field=models.BigIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="financialdocument",
            name="operating_cash_flow",
            field=models.BigIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="financialdocument",
            name="revenue",
            field=models.BigIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="financialdocument",
            name="total_assets",
            field=models.BigIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="financialdocument",
            name="total_liabilities",
            field=models.BigIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="financialindicator",
            name="debt_ratio",
            field=models.DecimalField(
                blank=True, decimal_places=4, max_digits=10, null=True
            ),
        ),
        migrations.AlterField(
            model_name="financialindicator",
            name="free_cash_flow",
            field=models.DecimalField(
                blank=True, decimal_places=2, max_digits=15, null=True
            ),
        ),
        migrations.AlterField(
            model_name="financialindicator",
            name="gross_profit_margin",
            field=models.DecimalField(
                blank=True, decimal_places=4, max_digits=10, null=True
            ),
        ),
        migrations.AlterField(
            model_name="financialindicator",
            name="net_profit_margin",
            field=models.DecimalField(
                blank=True, decimal_places=4, max_digits=10, null=True
            ),
        ),
    ]

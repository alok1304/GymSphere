# Generated by Django 4.2.18 on 2025-01-23 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_plan_planfeature'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plan',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]

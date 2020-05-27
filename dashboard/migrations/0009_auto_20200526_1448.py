# Generated by Django 3.0.6 on 2020-05-26 14:48

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0008_auto_20200524_1348'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicalrecord',
            name='h2_plasma_glucose',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=4, validators=[django.core.validators.MinValueValidator(0.01)]),
        ),
    ]

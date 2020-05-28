# Generated by Django 3.0.6 on 2020-05-27 14:50

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0011_auto_20200527_1301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicalrecord',
            name='fasting_plasma_glucose',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=4, null=True, validators=[django.core.validators.MinValueValidator(0.01)]),
        ),
        migrations.AlterField(
            model_name='medicalrecord',
            name='h2_plasma_glucose',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=4, null=True, validators=[django.core.validators.MinValueValidator(0.01)]),
        ),
        migrations.AlterField(
            model_name='medicalrecord',
            name='hbA1c',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=4, null=True, validators=[django.core.validators.MinValueValidator(0.01)]),
        ),
    ]

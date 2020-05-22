# Generated by Django 3.0.6 on 2020-05-22 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0005_nutritionintake_server_size'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicalrecord',
            name='fasting_plasma_glucose',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=4),
        ),
        migrations.AlterField(
            model_name='medicalrecord',
            name='h2_plasma_glucose',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=4),
        ),
        migrations.AlterField(
            model_name='medicalrecord',
            name='hbA1c',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=4),
        ),
    ]

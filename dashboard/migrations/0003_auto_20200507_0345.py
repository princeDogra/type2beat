# Generated by Django 3.0.5 on 2020-05-07 03:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_auto_20200507_0301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fooditem',
            name='allergens',
            field=models.TextField(max_length=500),
        ),
        migrations.AlterField(
            model_name='fooditem',
            name='ingredients_text',
            field=models.TextField(max_length=500),
        ),
    ]

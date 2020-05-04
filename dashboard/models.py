from django.db import models

# Create your models here.

class GlucoseTracker(models.Model):
    product_name = models.CharField(max_length=100)
    ingredients_text = models.CharField(max_length=500)
    allergens = models.CharField(max_length=500)
    serving_size = models.CharField(max_length=100)
    fat_100g = models.DecimalField(max_digits=8, decimal_places=4, blank=True)
    cholesterol_100g = models.DecimalField(max_digits=8, decimal_places=4, blank=True)
    carbohydrates_100g = models.DecimalField(max_digits=8, decimal_places=4, blank=True)
    sugars_100g = models.DecimalField(max_digits=8, decimal_places=4, blank=True)
    fiber_100g = models.DecimalField(max_digits=8, decimal_places=4, blank=True)
    proteins_100g = models.DecimalField(max_digits=8, decimal_places=4, blank=True)
    salt_100g = models.DecimalField(max_digits=8, decimal_places=4, blank=True)
    sodium_100g = models.DecimalField(max_digits=8, decimal_places=4, blank=True)
    alcohol_100g = models.DecimalField(max_digits=8, decimal_places=4, blank=True)
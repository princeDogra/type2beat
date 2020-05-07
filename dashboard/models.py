from django.db import models


class FoodItem(models.Model):
    product_name = models.TextField(blank=False)
    ingredients_text = models.TextField(blank=True)
    allergens = models.TextField(blank=True)
    serving_size = models.TextField(blank=True)
    fat_100g = models.DecimalField(max_digits=11, decimal_places=6, blank=True)
    cholesterol_100g = models.DecimalField(max_digits=11, decimal_places=6, blank=True)
    carbohydrates_100g = models.DecimalField(max_digits=11, decimal_places=6, blank=True)
    sugars_100g = models.DecimalField(max_digits=11, decimal_places=6, blank=True)
    fiber_100g = models.DecimalField(max_digits=11, decimal_places=6, blank=True)
    proteins_100g = models.DecimalField(max_digits=11, decimal_places=6, blank=True)
    salt_100g = models.DecimalField(max_digits=11, decimal_places=6, blank=True)
    sodium_100g = models.DecimalField(max_digits=11, decimal_places=6, blank=True)
    alcohol_100g = models.DecimalField(max_digits=11, decimal_places=6, blank=True)

    def __str__(self):
        return self.product_name

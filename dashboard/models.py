from django.db import models
from django.contrib.auth import get_user_model

class FoodItem(models.Model):
    id = models.AutoField(primary_key=True)
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

class MedicalRecord(models.Model):
    timestamp = models.DateField(blank=False)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    h2_plasma_glucose = models.DecimalField(max_digits=4, decimal_places=2, blank=True, default=0.0)
    fasting_plasma_glucose = models.DecimalField(max_digits=4, decimal_places=2, blank=True, default=0.0)
    hbA1c = models.DecimalField(max_digits=4, decimal_places=2, blank=True, default=0.0)

    def __str__(self):
        return (self.user.username + ' - ' + str(self.timestamp))

class NutritionIntake(models.Model):
    food = models.ForeignKey(FoodItem, on_delete=models.CASCADE)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    server_size = models.PositiveSmallIntegerField(default=1)
    timestamp = models.DateTimeField(blank=False, null=False)

    def __str__(self):
        return ('{username} - {food} - {date}').format(username=self.user.username, food=self.food.product_name, date=self.timestamp)

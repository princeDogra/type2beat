from  rest_framework import serializers
from dashboard.models import FoodItem, NutritionIntake

class FoodItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodItem
        fields = ('id', 'product_name', 'ingredients_text', 'allergens', 'serving_size',
                    'fat_100g', 'cholesterol_100g', 'carbohydrates_100g', 'sugars_100g',
                    'fiber_100g', 'proteins_100g', 'salt_100g', 'sodium_100g', 'alcohol_100g')


class NutritionIntakeSerializer(serializers.ModelSerializer):
    class Meta:
        model = NutritionIntake
        fields = ('food', 'user', 'meal_type', 'timestamp')

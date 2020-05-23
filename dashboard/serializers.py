from  rest_framework import serializers
from dashboard.models import FoodItem, NutritionIntake, MedicalRecord

class FoodItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodItem
        fields = ('id', 'product_name', 'serving_size',
                    'fat_100g', 'carbohydrates_100g', 'sugars_100g',
                    'fiber_100g', 'proteins_100g', 'salt_100g', 'sodium_100g', 'alcohol_100g')


class NutritionIntakeSerializer(serializers.ModelSerializer):
    class Meta:
        model = NutritionIntake
        fields = ('food', 'user', 'meal_type', 'timestamp')

class MedialRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalRecord
        fields = ('timestamp', 'h2_plasma_glucose', 'fasting_plasma_glucose', 'hbA1c')

from django.contrib import admin
from .models import FoodItem,MedicalRecord

# register the FoodItem model
admin.site.register(FoodItem)
admin.site.register(MedicalRecord)

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from .models import FoodItem, MedicalRecord, NutritionIntake
from .forms import MedicalForm

@login_required
def dashboard(request):
    return render(request, 'dashboard.html')

@login_required
def glucose(request):
    if request.method == 'POST':
        nutrition_intake = NutritionIntake()
        foodItems = request.POST['foodItems']
        timestamp = request.POST['mealDate']
        meal_type = request.POST['mealType']
        for item in foodItems.split(" "):
            nutrition_intake.food = FoodItem.objects.get(pk=int(item))
            nutrition_intake.timestamp = timestamp
            nutrition_intake.meal_type = meal_type
            nutrition_intake.user =  request.user
            nutrition_intake.save()
            messages.success(request, f'Successfully recorded values')
        return redirect('glucose')
    else:
        return render(request, 'glucose.html')

@login_required
def medical(request):
    if request.method == 'POST':
        form = MedicalForm(request.POST)
        form.instance.user = request.user
        if form.is_valid():
            messages.success(request, f'Successfully recorded values')
            form.save()
        return redirect('medical')
    else:
        form = MedicalForm()
        return render(request, 'medical.html', {'medicalform' : form})

@login_required
def reminder(request):
    return render(request, 'reminder.html')


@login_required
def food(request):
    return render(request,'food.html')

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from .models import FoodItem, MedicalRecord, NutritionIntake
from .forms import MedicalForm
from django.views import View

@login_required
def dashboard(request):
    return render(request, 'dashboard.html')

@login_required
def glucose(request):
    if request.method == 'POST':
        nutrition_intake = NutritionIntake()
        foodItems = request.POST['foodItems']
        timestamp = request.POST['mealTimestamp']
        timestamp = timestamp[:-3]
        from datetime import datetime
        timestamp = datetime.strptime(timestamp, "%m/%d/%Y %H:%M")
        server_size = request.POST['serveSize']
        for item in foodItems.split(" "):
            nutrition_intake.food = FoodItem.objects.get(pk=int(item))
            nutrition_intake.timestamp = timestamp
            nutrition_intake.server_size = server_size
            nutrition_intake.user =  request.user
            nutrition_intake.save()
        messages.success(request, f'Successfully recorded your meal intake')
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
        else:
            if float(request.POST['h2_plasma_glucose']) < 0:
                messages.error(request, f'Value should be positive')
            return redirect('medical')
        return redirect('medical')
    else:
        from datetime import date
        today = date.today()

        form = MedicalForm()
        return render(request, 'medical.html', {'medicalform' : form})

@login_required
def reminder(request):
    return render(request, 'reminder.html')


@login_required
def food(request):
    return render(request,'food.html')


@login_required
def history(request):
    return render(request, 'history.html')

def HistoryView(View):
    template_name = 'history.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

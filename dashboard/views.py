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
        from datetime import datetime
        queryset = MedicalRecord.objects.filter(user=request.user, timestamp__startswith=datetime.strptime(request.POST['timestamp'], "%Y-%m-%d").date())
        if queryset:
            messages.error(request, f'Record with similar date exists')
            return redirect('medical')
        else:
            if form.is_valid():
                messages.success(request, f'Successfully recorded values')
                form.save()
            else:
                if datetime.strptime(request.POST['timestamp'], "%Y-%m-%d") > datetime.today():
                    messages.error(request, f'Selected date cannot be greater than today\'s date')
                elif float(request.POST['h2_plasma_glucose']) < 0:
                    messages.error(request, f'2H Plasma Glucose Value should be positive')
                elif float(request.POST['fasting_plasma_glucose']) < 0:
                    messages.error(request, f'Fasting Plasma Glucose Value should be positive')
                elif float(request.POST['hbA1c']) < 0:
                    messages.error(request, f'HbA1c Value should be positive')
                elif float(request.POST['hbA1c']) == 0.0 and float(request.POST['fasting_plasma_glucose']) == 0.0 and float(request.POST['h2_plasma_glucose']) == 0.0:
                    messages.error(request, f'All Parameter values cannot be empty')
                else:
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


@login_required
def history(request):
    return render(request, 'history.html')

def HistoryView(View):
    template_name = 'history.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from .models import FoodItem, MedicalRecord
from .forms import MedicalForm

@login_required
def dashboard(request):
    return render(request, 'dashboard.html')

@login_required
def glucose(request):
    context = None
    queryset = []
    query = request.GET.get('q')
    if query:
        fooditems = FoodItem.objects.filter(Q(product_name__icontains=query)).distinct()
        for fooditem in fooditems:
            queryset.append(fooditem)
        context = {'items' : queryset}
    return render(request, 'glucose.html', context)

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

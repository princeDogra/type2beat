from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from .models import FoodItem, MedicalRecord
from .forms import MedicalForm

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication, BasicAuthentication

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


class MedicalChartData(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def generate_data(self, request):
        queryset = MedicalRecord.objects.filter(user=request.user).order_by('timestamp')
        data = {'labels':[], 'Fasting Plasma Glucose': [], '2-h Plasma Glucose':[], 'HbA1c': []}
        for items in queryset:
            data['labels'].append(str(items.timestamp))
            data['Fasting Plasma Glucose'].append(items.fasting_plasma_glucose)
            data['2-h Plasma Glucose'].append(items.h2_plasma_glucose)
            data['HbA1c'].append(items.hbA1c)
        return data

    def get(self, request, format=None):
        data = self.generate_data(request)
        labels = data['labels']
        default_items = [
        {
            'label': 'Fasting Plasma Glucose',
            'backgroundColor': 'rgba(0, 63, 92, 1)',
            'data': data['Fasting Plasma Glucose']
        },
        {
            'label': "2-h Plasma Glucose",
            'backgroundColor': 'rgba(188, 80, 144, 1)',
            'data': data['2-h Plasma Glucose']
        },
        {
            'label': "HbA1c",
            'backgroundColor': 'rgba(255, 166, 0, 1)',
            'data': data['HbA1c']
        }]
        data = {
            "labels": labels,
            "datasets": default_items,
        }
        return Response(data)

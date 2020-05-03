from django.shortcuts import render

def dash_landing(request):
    return render(request, 'dashboard.html')

def glucose_dash(request):
    return render(request, 'glucose-dash.html')
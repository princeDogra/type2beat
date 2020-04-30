from django.shortcuts import render

def dash_landing(request):
    return render(request, 'dashboard.html')

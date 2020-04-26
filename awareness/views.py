from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def contacts(request):
    return render(request, 'contacts.html')

def exercises(request):
    return render(request, 'exercises.html')

def healthy_diets(request):
    return render(request, 'healthy_diets.html')

def prevention(request):
    return render(request, 'prevention.html')

def services(request):
    return render(request, 'services.html')
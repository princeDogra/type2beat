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

def water(request):
    return render(request, 'water.html')

def fast(request):
    return render(request, 'fast.html')

def diabetes(request):
    return render(request, 'diabetes.html')

def negativeDiabetes(request):
    return render(request, 'negativeDiabetes.html')

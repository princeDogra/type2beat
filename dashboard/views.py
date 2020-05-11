from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import FoodItem

@login_required
def dashboard(request):
    return render(request, 'dashboard.html')

@login_required
def glucose(request):
    context = None
    queryset = []
    query = request.GET.get('q')
    if query:
        # for advanced search
        # queries = query.split(" ") # corned beef = ["corned", "beef"]
        # for q in queries:
        #     fooditems = FoodItem.objects.filter(Q(product_name__icontains=q)).distinct()
        #
        #     for fooditem in fooditems:
        #         queryset.append(fooditem)
        fooditems = FoodItem.objects.filter(Q(product_name__icontains=query)).distinct()
        for fooditem in fooditems:
            queryset.append(fooditem)
        # print(f'query set is as follows: {type(queryset[0])}')
        context = {'items' : queryset}
    return render(request, 'glucose.html', context)

@login_required
def medical(request):
    return render(request, 'medical.html')

@login_required
def reminder(request):
    return render(request, 'reminder.html')

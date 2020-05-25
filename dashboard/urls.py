"""type2beat URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from dashboard import views as dash_views
from dashboard import api_views as dash_api_views

urlpatterns = [
    url(r'^dashboard/', dash_views.dashboard, name='dashboard'),
    url(r'^glucose/', dash_views.glucose, name='glucose'),
    url(r'^medical/', dash_views.medical, name='medical'),
    url(r'^reminder/', dash_views.glucose, name='reminder'),
    url(r'^api/chart/data/medical', dash_api_views.MedicalChartData.as_view()),
    url(r'^api/chart/data/glucose', dash_api_views.NutritionIntakeChartData.as_view()),
    url(r'^api/data/food/', dash_api_views.FoodItemList.as_view()),
    url(r'^api/data/nutrition',dash_api_views.NutritionIntakeData.as_view()),
    url(r'^api/data/medical', dash_api_views.MedicalData.as_view()),
    url(r'^food/', dash_views.food, name='food'),
    url(r'^hiistory/', dash_views.history, name='history'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

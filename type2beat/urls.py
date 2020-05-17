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
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from awareness import views as awareness_views
from dashboard import views as dash_views
from users import views as user_views
from dashboard.api_views import MedicalChartData,NutritionIntakeChartData, MedicalData
from dashboard import api_views as dashboard_api_views

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', awareness_views.index, name='home'),
    url(r'^contacts/', awareness_views.contacts, name='contacts'),
    url(r'^exercises/', awareness_views.exercises, name='exercises'),
    url(r'^healthy_diets/', awareness_views.healthy_diets, name='healthy_diets'),
    url(r'^prevention/', awareness_views.prevention, name='prevention'),
    url(r'^services/', awareness_views.services, name='services'),
    url(r'^water/', awareness_views.water, name="water"),
    url(r'^fast/', awareness_views.fast, name="fast"),
    url(r'^diabetes/', awareness_views.diabetes, name="diabetes"),
    url(r'^dashboard/', dash_views.dashboard, name='dashboard'),
    url(r'^glucose/', dash_views.glucose, name='glucose'),
    url(r'^impact', awareness_views.impact,name='impact'),
    url(r'^heart', awareness_views.heart,name='heart'),
    url(r'^eyes', awareness_views.eyes,name="eyes"),
    url(r'^kidney', awareness_views.kidney,name="kidney"),
    url(r'^nerves', awareness_views.nerves,name='nerves'),
    url(r'^digestion',awareness_views.digestion,name ='digestion'),
    url(r'^skin',awareness_views.skin,name='skin'),
    url(r'^medical/', dash_views.medical, name='medical'),
    url(r'^reminder/', dash_views.glucose, name='reminder'),
    url(r'^register/', user_views.register, name='register'),
    url(r'^login/', user_views.login, name='login'),
    url(r'^logout/', user_views.logout, name='logout'),
    url(r'^api/chart/data/medical', MedicalChartData.as_view()),
    url(r'^api/chart/data/glucose', NutritionIntakeChartData.as_view()),
    url(r'^api/data/food/', dashboard_api_views.FoodItemList.as_view()),
    url(r'^api/data/medical', MedicalData.as_view()),
    url(r'^food/', dash_views.food, name='food'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

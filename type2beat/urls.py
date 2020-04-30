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
from awareness import views as awareness_views
from dashboard import views as dash_views

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', awareness_views.index, name='home'),
    url(r'^contacts/', awareness_views.contacts, name='contacts'),
    url(r'^exercises/', awareness_views.exercises, name='exercises'),
    url(r'^healthy_diets/', awareness_views.healthy_diets, name='healthy_diets'),
    url(r'^prevention/', awareness_views.prevention, name="prevention"),
    url(r'^services/', awareness_views.services, name="services"),
    url(r'^dashboard/', dash_views.dash_landing, name="dash-landing"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

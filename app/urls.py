"""
URL configuration for app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include
from django.http import HttpResponse
from django_prometheus import exports

def trigger_error(request):
    division_by_zero = 1 / 0

def home_view(request):
    return HttpResponse("Bienvenue sur la page d'accueil de mon app Django By Yomna Jemail !")

urlpatterns = [
    path('', home_view, name='home'),
    path('admin/', admin.site.urls),
    # path("super-admin/", admin.site.urls),
    path('sentry-debug/', trigger_error),
    # path('metrics/', include('django_prometheus.urls')),
    path('', include('django_prometheus.urls')), #Cela ajoute les URLs internes de django_prometheus, y compris /metrics, directement à la racine.

]

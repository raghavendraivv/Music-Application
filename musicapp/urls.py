from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from music import views
from django import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/',include('accounts.urls')),
    path('music/',include('music.urls')),
    path('accounts/',include('django.contrib.auth.urls')),
    path('',TemplateView.as_view(template_name='main.html'),name='main'),
]

from . import views
from django.urls import path

urlpatterns = [
    path('', views.translatorView, name='translatorView')
]
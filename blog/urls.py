from . import views
from django.urls import path

urlpatterns = [
    path('<slug:slug>', views.blogView.as_view(), name='blogView'),
    path('about/', views.aboutView.as_view(), name='aboutView')
]
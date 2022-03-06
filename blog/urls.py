from . import views
from django.urls import path

urlpatterns = [
    path('<slug:slug>', views.blogView.as_view(), name='blogView')
]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add/', views.add, name='add_employee'),
    path('list/', views.list_employees, name='list_employees'),
]

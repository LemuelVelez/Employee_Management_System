from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add/', views.add, name='add_employee'),
    path('edit/<int:employee_id>/', views.edit_employee, name='edit_employee'),
    path('list/', views.list_employees, name='list_employees'),
    path('delete_employee/<int:employee_id>/', views.delete_employee, name='delete_employee'),
]

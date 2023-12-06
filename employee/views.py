from django.shortcuts import render, redirect
from .forms import EmployeeForm
from .models import Employee
from django.contrib import messages

def home(request):
    return render(request, 'employee/index.html')

def list_employees(request):
    employees = Employee.objects.all()
    return render(request, 'employee/list_employees.html', {'employees': employees})

def add(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            new_firstname = form.cleaned_data['firstname']
            new_middle = form.cleaned_data['middle']
            new_lastname = form.cleaned_data['lastname']
            new_gender = form.cleaned_data['gender']

            new_employee = Employee(
                firstname=new_firstname,
                lastname=new_lastname,
                middle=new_middle,
                gender=new_gender
            )
            new_employee.save()

            # Show success message
            messages.success(request, 'Employee added successfully')
            return render(request, 'employee/add_employee.html', {'form': form})

    else:
        form = EmployeeForm()
        form.field_order = None
        return render(request, 'employee/add_employee.html', {'form': form})

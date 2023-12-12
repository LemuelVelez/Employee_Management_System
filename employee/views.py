from django.shortcuts import render, redirect, get_object_or_404
from .forms import EmployeeForm
from .models import Employee
from django.contrib import messages
from django.http import JsonResponse

def home(request):
    return render(request, 'employee/index.html')

def list_employees(request):
    employees = Employee.objects.all()
    return render(request, 'employee/list_employees.html', {'employees': employees})

def add(request, employee_id=None):
    if employee_id:
        # If employee_id is provided, it's an edit request
        employee = get_object_or_404(Employee, pk=employee_id)
    else:
        employee = None

    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()

            # Show success message
            messages.success(request, 'Employee added successfully')

    else:
        form = EmployeeForm(instance=employee)

    return render(request, 'employee/add_employee.html', {'form': form, 'employee': employee})

def delete_employee(request, employee_id):
    employee = get_object_or_404(Employee, pk=employee_id)
    employee.delete()
    messages.success(request, 'Employee deleted successfully')
    return redirect('list_employees')

# Updated view for editing employees
def edit_employee(request, employee_id):
    employee = get_object_or_404(Employee, pk=employee_id)

    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True})
    else:
        form = EmployeeForm(instance=employee)

    return render(request, 'employee/edit_employee.html', {'form': form, 'employee': employee})

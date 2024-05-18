# views.py
from django.shortcuts import render
from .models import Employee

def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'payroll/employee_list.html', {'employees': employees})

def calculate_payroll(request):
    employees = Employee.objects.all()
    total_salary = sum(employee.salary for employee in employees)
    return render(request, 'payroll/payroll_summary.html', {'total_salary': total_salary})
# views.py
from django.shortcuts import render
from .models import Employee

def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'payroll/employee_list.html', {'employees': employees})

def calculate_payroll(request):
    employees = Employee.objects.all()
    total_salary = sum(employee.salary for employee in employees)
    return render(request, 'payroll/payroll_summary.html', {'total_salary': total_salary})

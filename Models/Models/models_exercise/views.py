from django.shortcuts import render, get_object_or_404, redirect

from Models.models_exercise.models import Employee, Department


def index(request):
    x = list(Employee.objects.all())
    context = {
        'employees': Employee.objects.all()
    }
    return render(request, 'index.html', context)


def department_details(request, pk):
    context = {
        'department': get_object_or_404(Department, pk=pk)
    }

    return render(request, 'department_details.html', context)


def delete_employee(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    employee.delete()
    return redirect('index')

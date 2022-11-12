from django.shortcuts import render
from django import http

from Django101.tasks.models import Task


# Create your views here.
def show_bare_minimum_view(request):
    return http.HttpResponse('It works')


def get_all_tasks(request):
    all_tasks = Task.objects.all()
    result = ', '.join(f'{t.name}({t.id})' for t in all_tasks)
    # [nam(id), name(id)]
    return http.HttpResponse(result)


def index(request):
    all_tasks = Task.objects.order_by('id').all()
    context = {
        'title': 'The tasks app!',
        'tasks': all_tasks,
    }
    return render(request, 'index.html', context)

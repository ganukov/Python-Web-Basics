import random
from datetime import datetime

from django.shortcuts import render, redirect


class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_info(self):
        return f'{self.name},{self.age}'


def index(request):
    context = {
        'title': 'softuni Homepage',
        'value': random.random(),
        'info': {
            'address': 'Sofia'
        },
        'student': Student('Georgi', 31),
        'now': datetime.now(),
        'students': [],
        'values': list(range(20)),
    }
    return render(request, 'index.html', context)


def redirect_to_home(request):
    return redirect('index')


def about(request):
    return render(request, 'about.html')

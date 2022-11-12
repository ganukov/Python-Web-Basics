from django.http import HttpResponse, HttpRequest
from django.shortcuts import render


# Create your views here.

def show_departments(request, *args, **kwargs):
    body = f'path: {request.path},args = {args}, kwargs={kwargs}'
    return HttpResponse(body)


def show_department_details(request, department_id):
    body = f'args : {request.path}, id: {department_id}'
    return HttpResponse(body)

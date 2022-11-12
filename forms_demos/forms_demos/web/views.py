from django import forms
from django.shortcuts import render
from forms_demos.web.forms import NameForm
from forms_demos.web.models import Person


def index(request):
    name = None
    if request.method == 'GET':
        form = NameForm()
    else:
        form = NameForm(request.POST)
        form.is_valid()
        name = form.cleaned_data['name']
        Person.objects.create(
            name=name,
        )
    context = {
        'form': form,
        'name': name,
    }
    return render(request, 'index.html', context)


def index_model_form(request):
    pass

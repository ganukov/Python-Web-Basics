from django import forms
from django.core.exceptions import ValidationError
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def validate_priority(value):
    if value < 1 or 10 < value:
        raise ValidationError("Priority must be between 1 and 10")
def validate_text(value):
    # if valid:
    #   do nothing
    # else:
    #   raise ValidationExeption()
    if '_' in value:
        raise ValidationError("'_' is invalid character for 'text'")
class TodoForm(forms.Form):
    text = forms.CharField(
        validators=(validate_text,
                    )
    )
    is_done = forms.BooleanField()
    priority = forms.IntegerField(
        validators=(validate_priority,
                    )
    )

def index(request):
    if request.method == 'GET':
        form = TodoForm()
    else:
        form = TodoForm(request.POST)

        if form.is_valid():
            return HttpResponse('All is valid')

    context = {
        'form':form,
    }
    return render(request,'index.html',context)
from django.urls import path

from Models.models_exercise.views import index, delete_employee , department_details

urlpatterns = (
    path('',index,name='index'),
    path('delete/<int:pk>/',delete_employee,name='delete employee'),
    path('department/<int:pk>',department_details,name='details department'),
)
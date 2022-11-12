from django.urls import path

from departments_app.departments.views import show_departments, show_department_details

urlpatterns = (
    path('', show_departments,name='show departments'),  # /departments/
    path('<department_id>/', show_department_details),  # /departments/{ID}/
    path('int/<int:department_id>/', show_department_details), # /departments/int/{ID}/

)

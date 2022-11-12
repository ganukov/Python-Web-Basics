from django.urls import path

from Django101.tasks.views import show_bare_minimum_view, get_all_tasks, index

urlpatterns = (
    path('',index),
    path('', show_bare_minimum_view),
    # http://localhost:8001/tasks/all
    path('all/',get_all_tasks)
)
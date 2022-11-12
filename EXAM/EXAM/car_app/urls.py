from EXAM.car_app.views import index, profile_create, profile_details, profile_edit, profile_delete, \
    car_create, car_details, car_edit, car_delete, catalogue
from django.urls import path, include

urlpatterns = (
    path('', index, name='index page'),
    path('catalogue/', catalogue, name='catalogue page'),
    path('profile/', include([
        path('create', profile_create, name='profile create page'),
        path('details/', profile_details, name='profile details page'),
        path('edit/', profile_edit, name='profile edit page'),
        path('delete/', profile_delete, name='profile delete page'),
    ])),
    path('car/', include([
        path('create/', car_create, name='car create page'),
        path('<int:car_id>/details/', car_details, name='car details page'),
        path('<int:car_id>/edit/', car_edit, name='car edit page'),
        path('<int:car_id>/delete/', car_delete, name='car delete page'),

    ])),
)

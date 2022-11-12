from django.urls import path, include
from petstagram.photos import views

urlpatterns = [
    path('add/',views.add_photo,name='add-photo'),
    path('<int:id>/',include([
        path('',views.show_photo_details,name='photo-details'),
        path('edit/',views.edit_photo,name='edit-photo'),
        ]))
]
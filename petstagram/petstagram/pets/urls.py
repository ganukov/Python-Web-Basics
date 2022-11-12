from django.urls import path, include
from petstagram.pets import views

urlpatterns = [
    path('add/',views.add_pet,name='add-pet'),
    path('<str:username>/pet/<slug:petname>/',include([
        path('',views.show_pet_details,name='pet-details'),
        path('edit/',views.edit_pet,name='pet-photo'),
        path('delete/',views.delete_pet,name='delete-pet'),
        ]))
]
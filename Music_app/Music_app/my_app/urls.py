from Music_app.my_app.views import home_page, add_album, album_details, edit_album, delete_album, profile_details, \
    profile_delete
from django.urls import path, include

urlpatterns = (
    path('',home_page,name='home-page'),
    path('album/',include([
        path('add/',add_album,name='add-album'),
        path('details/<int:pk>/',album_details,name='details'),
        path('edit/<int:pk>/',edit_album,name='edit'),
        path('delete/<int:pk>/',delete_album,name='delete')
    ])),
    path('profile/',include([
        path('details/',profile_details,name='profile-details'),
        path('delete/',profile_delete,name='profil-delete'),
    ]))
)
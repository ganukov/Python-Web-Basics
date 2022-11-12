from M_app.web.views import home_page, details_album, edit_album, delete_album, profile_details, profile_deletion, \
    add_album
from django.urls import path, include

urlpatterns = (
    path('', home_page, name='home page'),
    path('album/', include([
        path('add/', add_album, name='add album page'),
        path('details/<int:album_id>/', details_album, name='album details page'),
        path('edit/<int:album_id>', edit_album, name='edit album page'),
        path('delete/<int:album_id>', delete_album, name='delete album page'),
    ])),
    path('profile/', include([
        path('details/', profile_details, name='profile details page'),
        path('delete/', profile_deletion, name='delete profile page'),
    ]))
)

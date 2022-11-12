from NOTES.notes_app.views import home_page, add_note, delete_note, edit_note, details_note, profile_page
from django.urls import path

urlpatterns = (
    path('', home_page, name='home page'),
    path('add', add_note, name='add note page'),
    path('edit/<int:note_id>', edit_note, name='edit note page'),
    path('delete/<int:note_id>', delete_note, name='delete note page'),
    path('details/<int:note_id>', details_note, name='note details page'),
    path('profile', profile_page, name='profile page'),
)

from Online_library.Library.views import home_page, add_book, edit_book, details_book, profile_edit, profile_delete, \
    profile_details, delete_book
from django.urls import path, include

urlpatterns = (
    path('', home_page, name='home page'),
    path('add/', add_book, name='add book page'),
    path('edit/<int:book_id>', edit_book, name='edit book page'),
    path('details/<int:book_id>', details_book, name='book details page'),
    path('delete/<int:book_id>',delete_book,name='delete book page'),

    path('profile/', profile_details, name='profile page'),
    path('profile/', include([path('edit/', profile_edit, name='edit profile page'),
                              path('delete/', profile_delete, name='delete profile page'), ]))

)

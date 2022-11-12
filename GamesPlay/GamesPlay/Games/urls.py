from GamesPlay.Games.views import home_page, dashboard, game_create, game_details, game_edit, game_delete, \
    profile_create, profile_details, profile_edit, profile_delete
from django.urls import path, include

urlpatterns = (path('', home_page, name='home page'),
               path('dashboard/', dashboard, name='dashboard page'),
               path('game/', include([
                   path('create/', game_create, name='create game page'),
                   path('details/<int:game_id>/', game_details, name='details game page'),
                   path('edit/<int:game_id>/', game_edit, name='edit game page'),
                   path('delete/<int:game_id>/', game_delete, name='delete game page'),
               ])),
               path('profile/', include([
                   path('create/', profile_create, name='create profile page'),
                   path('details/', profile_details, name='details profile page'),
                   path('edit/', profile_edit, name='edit profile page'),
                   path('delete/', profile_delete, name='delete profile page')
               ]))
               )

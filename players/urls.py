from django.urls import path
from . import views

urlpatterns = [
    path('players/', views.index, name='all-players'), # our-domain.com/players
    path('players/<slug:player_slug>', views.player_details, name='player-details'), # our-domain.com/players/<dynamic-path-segment>
]
from django.urls import path
from . import views

urlpatterns = [
    path(
        '<str:region>/<str:game_name>-<str:tag_line>/',
        views.summoner,
        name='summoner',
    )
]

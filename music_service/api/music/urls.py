from django.urls import path

from .views import ListSongView


urlpatterns = [
    path('songs/', ListSongView.as_view(), name='songs-all'),
]

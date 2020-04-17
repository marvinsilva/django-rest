from django.conf.urls import url
from myapi.myapp import views

urlpatterns = [
    url(r'^musics/$', views.MusicList.as_view(), name='music-list'),
]

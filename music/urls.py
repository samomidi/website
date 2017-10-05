from django.conf.urls import url
from . import views

app_name = 'music'
#This is the actuall app name on the left pane which is music.
#So clarifies when we call music:detail in the index it calls details of
# music app not any other app

urlpatterns = [
    # /music/
    url(r'^$', views.index, name='index'),

    # /music/album_id/
    url(r'^(?P<album_id>[0-9]+)/$', views.detail, name='detail'),

# /music/album_id/favorite/
    url(r'^(?P<album_id>[0-9]+)/favorite$', views.favorite, name='favorite'),


]
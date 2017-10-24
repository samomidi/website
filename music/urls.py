from django.conf.urls import url
from . import views

app_name = 'music'
#This is the actuall app name on the left pane which is music.
#So clarifies when we call music:detail in the index it calls details of
# music app not any other app

urlpatterns = [
    # /music/
    # TUT 29 url(r'^$', views.index, name='index'),
    url(r'^$', views.IndexView.as_view(), name='index'), #as_view() is predefinded as we need a fun since we changes to class

    url(r'^register/$', views.USerFormView.as_view(), name='register'),

    # /music/album_id/
    # TUT 29 url(r'^(?P<album_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    # PK above is since we need primary key as querying the DB so we replace with album_id

# After changing to class in Tut 29 we don't use fav function
# # /music/album_id/favorite/
#     url(r'^(?P<album_id>[0-9]+)/favorite$', views.favorite, name='favorite'),

    #/music/album/add/
    url(r'album/add/$', views.AlbumCreate.as_view(), name='album-add'),
    # No primary key as we are adding new album

    #/music/album/2/
    url(r'album/(?P<pk>[0-9]+)/$', views.AlbumUpdate.as_view(), name='album-update'),

    #/music/album/2/delete/
    url(r'album/(?P<pk>[0-9]+)/delete/$', views.AlbumDelete.as_view(), name='album-delete'),

]
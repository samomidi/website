from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.


class Album(models.Model):
    artist = models.CharField(max_length=250)
    album_tittle = models.CharField(max_length=500)
    genre = models.CharField(max_length=100)
    album_logo = models.FileField()


    def get_absolute_url(self):
        return reverse('music:detail', kwargs={'pk':self.pk})
    #when we addd a new album it take the primary key ^ and takes us to detail view page

    def __str__(self):
        return self.album_tittle + " - " + self.artist


class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    file_type = models.CharField(max_length=10)
    song_tittle = models.CharField(max_length=250)
    is_favorite = models.BooleanField(default=False)

    def __str__(self):
        return self.song_tittle

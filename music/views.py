#from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
# Tut 15 from django.template import loader
from django.shortcuts import render, get_object_or_404
from django.http import Http404


from .models import Album, Song

def index(request):
    all_albums = Album.objects.all()
    # Tut 15 template = loader.get_template('music/index.html') # here we load the template
    context = {
        'all_albums': all_albums,
    }
    '''
    Tut 14
    html = ''
    for album in all_albums:
        url = '/music/' + str(album.id) + '/'
        html += '<a href="' + url + '">' + album.album_tittle + '</a><br>'
    '''
    # Tut 15 return HttpResponse(template.render(context, request)) #whenever you have view you need to return something

    return render(request,'music/index.html', context)

#def index(request):
 #   return HttpResponse("<h1>This is the music homepage</h1>")

def detail(request, album_id):
  #Tut 16 return HttpResponse("<h2>details for album Id:" + str(album_id) + "</h2>")
    #It just returns the album ID which we don't want anymore

    '''

    TUT 21
    try:
        #album = Album.objects.get(pk=album_id)
        album = Album.objects.filter(id=album_id).get()
    except Album.DoesNotExist:
        raise Http404("Album Does not exist")
    '''
    # instead of above try clause we can include get_object_or_404
    album = get_object_or_404(Album, pk=album_id)

    return render(request, 'music/detail.html', {'album': album})


def favorite(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    #now check if the song exists
    try:
        selected_song = album.song_set.get(pk=request.POST['song'])

    except (KeyError, Song.DoesNotExist):
        return render(request, 'music/detail.html', {
            'album': album,
            'error_message': "you did not select a valid song!!!!",
        })
    else:
        if  selected_song.is_favorite:
            selected_song.is_favorite = False
            selected_song.save()
        else:
            selected_song.is_favorite = True
            selected_song.save()

    return render(request, 'music/detail.html', {'album': album})
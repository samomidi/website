from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login #loging keeps the user logged in while they are browsing
from django.core.urlresolvers import reverse_lazy
from django.views.generic import View
from .models import Album
from .forms import UserForm

class IndexView(generic.ListView):
    template_name = 'music/index.html'
    context_object_name = 'all_albums'
    # if we dont write the above list it return the variable to index.html on object_list var

    def get_queryset(self): #predefined function which queries the DB
        return Album.objects.all()

class DetailView(generic.DeleteView): #detail view of one object
    model = Album #model is predefined
    template_name = 'music/detail.html'

class AlbumCreate(CreateView):
    model = Album
    fields = ['artist', 'album_tittle', 'genre', 'album_logo']


class AlbumUpdate(UpdateView):
    model = Album
    fields = ['artist', 'album_tittle', 'genre', 'album_logo']


class AlbumDelete(DeleteView):
    model = Album
    success_url = reverse_lazy('music:index')

class USerFormView(View):
    form_class = UserForm
    template_name = 'music/registration_form.html'

    #display a blank form
    def get(self, request):
        form = self.form_class(None) #reference to the actual form
        return  render(request, self.template_name, {'form': form})

    # process form data
    def post(self, request):
        form = self.form_class(request.POST)# when user clicks submit

        if form.is_valid():

            user = form.save(commit=False) # creates a user object but stores locally locally not in DB

            # cleaned and normallised data, like Date
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            #returns user object if credentials are correct
            user = authenticate(username=username, passowrd=password)#checks for user nad password against DB to see if it exists

            if user is not None:

                if user.is_active:
                    login(request, user)
                    return redirect('music:index')
        # This is like else part. If the user is banned or can't login, returns back to the same form(no error)
        return render(request, self.template_name, {'form': form})




    '''

In TUT 29 we change all the things to objects and list of object but changing to class

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




    Tut 14:
    html = ''
    for album in all_albums:
        url = '/music/' + str(album.id) + '/'
        html += '<a href="' + url + '">' + album.album_tittle + '</a><br>'


    # Tut 15 return HttpResponse(template.render(context, request)) #whenever you have view you need to return something

    return render(request,'music/index.html', context)

#def index(request):
 #   return HttpResponse("<h1>This is the music homepage</h1>")

def detail(request, album_id):
  #Tut 16 return HttpResponse("<h2>details for album Id:" + str(album_id) + "</h2>")
    #It just returns the album ID which we don't want anymore



    TUT 21
    try:
        #album = Album.objects.get(pk=album_id)
        album = Album.objects.filter(id=album_id).get()
    except Album.DoesNotExist:
        raise Http404("Album Does not exist")




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
            #comment


    return render(request, 'music/detail.html', {'album': album})
    '''
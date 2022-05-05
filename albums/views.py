from django.shortcuts import render
from .models import Album
from .forms import AlbumForm


# Create your views here.
def list_albums(request):
    albums = Album.objects.all()
    return render(request, "albums/list_albums.html",
                {"albums": albums})
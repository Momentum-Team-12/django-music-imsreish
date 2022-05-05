from django.shortcuts import render, redirect, get_object_or_404
from .models import Album
from .forms import AlbumForm


# Create your views here.
def list_albums(request):
    albums = Album.objects.all()
    return render(request, "albums/list_albums.html",
                {"albums": albums})

def album_details(request, pk):
    album = get_object_or_404(Album, pk=pk)
    return render(request, "albums/album_details.html", {
        "album": album
    })
from django.shortcuts import render, redirect
from .forms import AlbumForm
from . import models
from . import forms

# Create your views here.
def add_album(request):
    if request.method == 'POST':
        form = AlbumForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_album')
    else:
        form = AlbumForm()
    return render(request, 'add_album.html', {'form': form})


def edit_album(request, id):
    post = models.Album.objects.get(pk=id)
    form = forms.AlbumForm(instance=post)
    if request.method == 'POST':
        form = forms.AlbumForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    return render(request, 'add_album.html', {'form': form})

def delete_album(request, id):
    post = models.Post.objects.get(pk=id)
    post.delete()
    return redirect('homepage')
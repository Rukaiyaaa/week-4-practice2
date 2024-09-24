from django.shortcuts import render, redirect
from .forms import AlbumForm
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView
from . import models
from . import forms

# Create your views here.
class AddAlbumView(CreateView):
    model = models.Album
    form_class = AlbumForm
    template_name = 'add_album.html'
    success_url = reverse_lazy('add_album')


class EditAlbumView(UpdateView):
    model = models.Album
    form_class = AlbumForm
    template_name = 'add_album.html'
    success_url = reverse_lazy('homepage')

    def get_object(self, queryset=None):
        return models.Album.objects.get(pk=self.kwargs['id'])

class DeleteAlbumView(DeleteView):
    model = models.Album
    template_name = 'confirm_delete.html'
    success_url = reverse_lazy('homepage')

    def get_object(self, queryset=None):
        return models.Album.objects.get(pk=self.kwargs['id'])
from django.shortcuts import render, redirect
from .forms import MusicianForm
from . import models
from . import forms

# Create your views here.
def add_musician(request):
    if request.method == 'POST':
        form = MusicianForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_musician')
    else:
        form = MusicianForm()
    return render(request, 'add_musician.html', {'form': form})


def edit_musician(request, id):
    post = models.Musician.objects.get(pk=id)
    form = forms.MusicianForm(instance=post)
    if request.method == 'POST':
        form = forms.MusicianForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    return render(request, 'add_musician.html', {'form': form})


def delete_musician(request, id):
    post = models.Post.objects.get(pk=id)
    post.delete()
    return redirect('homepage')
from django.shortcuts import render
from musician.models import Musician
from album.models import Album


def home(request):
    musicians = Musician.objects.all()
    context = {
        'musicians': musicians,
    }
    return render(request, 'home.html', context)
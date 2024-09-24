from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView
from .forms import MusicianForm
from .models import Musician  

class AddMusicianView(CreateView):
    model = Musician
    form_class = MusicianForm
    template_name = 'add_musician.html'
    success_url = reverse_lazy('add_musician')


class EditMusicianView(UpdateView):
    model = Musician
    form_class = MusicianForm
    template_name = 'add_musician.html'  # Reusing the same template for editing
    success_url = reverse_lazy('homepage')

    def get_object(self, queryset=None):
        return Musician.objects.get(pk=self.kwargs['id'])


class DeleteMusicianView(DeleteView):
    model = Musician
    template_name = 'confirm_delete.html'  # You can use a confirmation page template
    success_url = reverse_lazy('homepage')

    def get_object(self, queryset=None):
        return Musician.objects.get(pk=self.kwargs['id'])
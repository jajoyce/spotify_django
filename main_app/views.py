from django.shortcuts import render
from django.views import View # <- View class to handle requests
from django.http import HttpResponse # <- a class to handle sending a type of response
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse
from .models import Artist


# Create your views here.

class Home(TemplateView):
    template_name = "home.html"

class About(TemplateView):
    template_name = "about.html"

class ArtistList(TemplateView):
    template_name = "artist_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get("name")
        if name != None:
                context["artists"] = Artist.objects.filter(name__icontains = name)
                context["header"] = f'Searching for "{name}"'
        else:
                context["artists"] = Artist.objects.all()
                context["header"] = "Trending Artists"
        return context

class ArtistCreate(CreateView):
        model = Artist
        fields = ['name', 'img', 'bio', 'verified_artist']
        template_name = "artist_create.html"

        def get_success_url(self):
                return reverse('artist_detail', kwargs={'pk': self.object.pk})

class ArtistDetail(DetailView):
        model = Artist
        template_name = "artist_detail.html"

class ArtistUpdate(UpdateView):
        model = Artist
        fields = ['name', 'img', 'bio', 'verified_artist']
        template_name = "artist_update.html"

        def get_success_url(self):
                return reverse('artist_detail', kwargs={'pk': self.object.pk})

class ArtistDelete(DeleteView):
        model = Artist
        template_name = "artist_delete_confirmation.html"
        success_url = "/artists/"

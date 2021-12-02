from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView

from .models import Movie
# Create your views here.

class HomeView(ListView):
    template_name = "index.html"
    model = Movie
    context_object_name = "movies"

class CreateMovieView(CreateView):
    template_name = "create.html"
    model = Movie
    fields =  ["title", "year" ,"poster","rating"]
    success_url = '/'
    # exclude = ["slug"]
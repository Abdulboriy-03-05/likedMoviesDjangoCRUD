from django.shortcuts import render
from django.views.generic.base import View , TemplateView
from django.views.generic import ListView, DetailView,DeleteView
from django.views.generic.edit import CreateView, FormView, UpdateView
from django.urls import reverse
from .models import Movie, Category
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

class MovieDeleteView(DeleteView):
    model = Movie
    success_url = '/'

class MovieUpdateView(UpdateView):
    template_name = 'create.html'
    model = Movie
    fields = ["title", "year", "rating", "poster"]
    success_url = '/'

class TestTemplateView(TemplateView):
    template_name = 'test.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["movies"] = Movie.objects.all()
        return context

class MovieDetailView(DetailView):
    model = Movie
    template_name = 'detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all()
        return context


# class AddCategoryView(FormView):
#     template_name = 'create.html'
#     form_class = Category
#     # initial = {'name':"Write your category name"}
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["categories"] = Category.objects.all()
#         return context
#
#     def form_valid(self, form):
#         form.save()
#         return super().form_valid(form)
#
#     def get_form(self, form_class=None):
#         self.object = super().get_form(form_class)
#         return self.object
#
#     def get_success_url(self):
#         return reverse("movie:detail",self.object.cleaned_data["pk"].pk )







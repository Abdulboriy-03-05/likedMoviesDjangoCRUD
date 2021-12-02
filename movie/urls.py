from django.urls import path
from .import views
app_name = 'movie'
urlpatterns = [
    path("", views.HomeView.as_view(), name='home'),
    path("create/", views.CreateMovieView.as_view(), name="create")
]
from django.urls import path
from .import views
app_name = 'movie'
urlpatterns = [
    path("", views.HomeView.as_view(), name='home'),
    path("create/", views.CreateMovieView.as_view(), name="create"),
    path("test/", views.TestTemplateView.as_view(), name='test'),
    path("detail/<int:pk>", views.MovieDetailView.as_view(), name='detail'),
    path("delete/<int:pk>", views.MovieDeleteView.as_view(), name='delete'),
    path("update/<int:pk>", views.MovieUpdateView.as_view(), name='update'),

    # path("add/", views.AddCategoryView.as_view(), name='add')
]
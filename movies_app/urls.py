from django.urls import path
from . import views

app_name = "movies"
urlpatterns = [
    path("", views.index, name="index"),
    path("<int:page_num>/", views.movie_list, name="movies"),
    path("movies/<int:pk>/", views.MovieDetailView.as_view(), name="movie-detail"),
    path("actors/<int:actor_id>/", views.actor_detail, name="actor-detail"),
]

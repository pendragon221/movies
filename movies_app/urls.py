from django.urls import path
from . import views

app_name = "movies"
urlpatterns = [
    path("", views.IndexListView.as_view(), name="index"),
    path("movies/<int:pk>/", views.MovieDetailView.as_view(), name="detail"),
    path("actors/<int:actor_id>/", views.actor_detail, name="actor_detail"),
]

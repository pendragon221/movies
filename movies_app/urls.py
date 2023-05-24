from django.urls import path
from . import views

app_name = "movies"
urlpatterns = [
    path("", views.IndexListView.as_view(), name="index"),
    path("<int:pk>/", views.MovieDetailView.as_view(), name="detail"),
]

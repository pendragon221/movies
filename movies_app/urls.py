from django.urls import path, include
from . import views
from rest_framework import routers, serializers, viewsets
from .models import Movie, Actor


# Serializers define the API representation.
class MovieSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Movie
        fields = [
            "movie_title",
            "movie_description",
            "pub_date",
            "time_create",
        ]


# ViewSets define the view behavior.
class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r"movies-api", MovieViewSet)


app_name = "movies"
urlpatterns = [
    path("api/", include(router.urls)),
    path("", views.index, name="index"),
    path("movies/", views.MovieListView.as_view(), name="movies"),
    path("movies/<int:pk>/", views.MovieDetailView.as_view(), name="movie-detail"),
    path("actors/<int:actor_id>/", views.actor_detail, name="actor-detail"),
]

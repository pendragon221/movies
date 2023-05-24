from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse, Http404
from django.template import loader

from .models import Movie


def index(request):
    latest_movie_list = Movie.objects.order_by("-pub_date")[:5]
    context = {
        "latest_movie_list": latest_movie_list,
    }
    return render(request, "movies_app/index.html", context)


def detail(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    return render(request, "movies_app/detail.html", {"movie": movie})

from typing import Any, Dict
from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.http import HttpResponse, Http404
from django.template import loader
from django.urls import reverse_lazy
from django.views import generic
from django.core.paginator import Paginator
from django.contrib.auth.views import LoginView
from math import ceil
from .models import Movie, Actor
from .forms import *


class MovieListView(generic.ListView):
    model = Movie
    template_name = "movies_app/index.html"
    paginate_by = 3

    def get_queryset(self):
        return Movie.objects.order_by("-pub_date")[:5]


class MovieDetailView(generic.DetailView, generic.CreateView):
    model = Movie
    template_name = "movies_app/movie_detail.html"
    form_class = MovieCommentForm
    success_url = reverse_lazy('movies:movie-detail')



def actor_detail(request, actor_id):
    actor = get_object_or_404(Actor, pk=actor_id)
    context = {"actor": actor}
    template = "movies_app/actor_detail.html"
    return render(request, template, context)


def index(request):
    return redirect("movies:movies")


# def register(request):
#     return HttpResponse("register")


# def login(request):
#     if request.POST:
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             print(form.cleaned_data)
#     else:
#         form = LoginForm()
#     return render(request, "movies_app/login.html", {"form": form})


# def index(request):
#     movie_list = Movie.objects.order_by("-pub_date")[:5]
#     context = {
#         "movie_list": movie_list,
#     }
#     return render(request, "movies_app/index.html", context)
#
#
# def detail(request, movie_id):
#     movie = get_object_or_404(Movie, pk=movie_id)
#     return render(request, "movies_app/detail.html", {"movie": movie})

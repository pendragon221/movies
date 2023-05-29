from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.http import HttpResponse, Http404
from django.template import loader
from django.views import generic
from math import ceil

from .models import Movie, Actor

def index(request):
    return redirect('movies:movies', 1)

    
def movie_list(request, page_num):
    posts_on_page = 1
    movie_list = Movie.objects.order_by("-pub_date")[(page_num - 1) * posts_on_page:page_num * posts_on_page]
    total_pages = ceil(Movie.objects.all().count() / posts_on_page)
    template_name = "movies_app/index.html"
    context = {
        'movie_list': movie_list,
        'pages': range(1, total_pages + 1),
        'total_pages': total_pages,
        'current_page': page_num
    }
    return render(request, template_name, context)


class MovieDetailView(generic.DetailView):
    model = Movie
    template_name = "movies_app/movie_detail.html"


def actor_detail(request, actor_id):
    actor = Actor.objects.get(pk=actor_id)
    context = {"actor": actor}
    template = "movies_app/actor_detail.html"
    return render(request, template, context)


# class IndexListView(generic.ListView):
#     model = Movie
#     template_name = "movies_app/index.html"
#     context_object_name = "movie_list"

#     def get_queryset(self):
#         return Movie.objects.order_by("-pub_date")[:5]

  
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

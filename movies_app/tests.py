from django.test import TestCase

from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from .models import Movie


def create_movie_obj(title, description):
    return Movie.objects.create(movie_title=title, movie_description=description, pub_date=timezone.now())


class MovieModelTests(TestCase):
    def test_was_the_movie_details_shown(self):
        """
            Creates movie object and tests whether the movie details has been displayed
        """
        test_movie_title = "test movie" + timezone.now().__str__()
        movie = create_movie_obj(test_movie_title, "test description")
        url = reverse("movies:detail", args=(movie.pk,))
        response = self.client.get(url)
        self.assertContains(response, test_movie_title)
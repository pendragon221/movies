from django.db import models


class Movie(models.Model):
    movie_title = models.CharField(max_length=200)
    movie_description = models.TextField()
    pub_date = models.DateTimeField("date published")

    def __str__(self):
        return self.movie_title


class Actor(models.Model):
    name = models.CharField(max_length=100)
    movie = models.ForeignKey(Movie, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name

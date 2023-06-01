from django.db import models
from django.contrib.auth.models import User


class Actor(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to="images/%Y/%m/%d/", blank=True)

    def __str__(self):
        return self.name


class Movie(models.Model):
    movie_title = models.CharField(max_length=200)
    movie_description = models.TextField()
    cast = models.ManyToManyField(Actor, blank=True)
    pub_date = models.DateTimeField("date published")
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    image = models.ImageField(upload_to="images/%Y/%m/%d/", blank=True)

    def __str__(self):
        return self.movie_title

class MovieComment(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    movie = models.ForeignKey(Movie, on_delete=models.DO_NOTHING)
    text = models.CharField(max_length=5000)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        if len(self.text) > 100:
            return self.text[:100]
        else:
            return self.text

# class MovieActor(models.Model):
#     movie = models.ForeignKey(to=Movie, on_delete=models.DO_NOTHING)
#     actor = models.ForeignKey(to=Actor, on_delete=models.DO_NOTHING)

#     def __str__(self):
#         return (
#             Movie.objects.get(pk=self.movie.pk).__str__()
#             + Actor.objects.get(pk=self.actor.pk).__str__()
#         )

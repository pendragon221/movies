from django.db import models


class Actor(models.Model):
    name = models.CharField(max_length=100)

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
    image = models.ImageField(upload_to="photos/%Y/%m/%d/", blank=True)

    def __str__(self):
        return self.movie_title


# class MovieActor(models.Model):
#     movie = models.ForeignKey(to=Movie, on_delete=models.DO_NOTHING)
#     actor = models.ForeignKey(to=Actor, on_delete=models.DO_NOTHING)

#     def __str__(self):
#         return (
#             Movie.objects.get(pk=self.movie.pk).__str__()
#             + Actor.objects.get(pk=self.actor.pk).__str__()
#         )

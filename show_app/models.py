from django.db import models
from django.urls import reverse

class Genre(models.Model):
  name = models.CharField(max_length=50)
  color = models.CharField(max_length=20)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse("genre_detail", kwargs={"pk": self.id})


class Show(models.Model):
  show= models.CharField(max_length=100)
  description = models.TextField(max_length=250)
  start_date = models.IntegerField()
  final_date = models.IntegerField()
  genre= models.ManyToManyField(Genre)

def __str__(self):
  return self.show

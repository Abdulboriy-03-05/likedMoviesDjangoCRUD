from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)

    def __str__(self):
        return f"{self.name}"

class Movie(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=100)
    poster = models.ImageField("Poster", upload_to='posters/')
    year = models.CharField(max_length=5)
    rating = models.FloatField(default=1.0)

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name_plural = "Movies"
        ordering = ["-id"]
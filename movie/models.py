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
        
class Movie_Shots(models.Model):
    title = models.CharField('Nomi', max_length=150, blank=True, null=True)
    desc = models.TextField("Kadr haqida", blank=True, null=True)
    image = models.ImageField('Kadr', upload_to="movie_shots/")
    movie = models.ForeignKey(Movie, verbose_name='Film',
                    on_delete=models.CASCADE,
                    null=True, blank=True)


    def __str__(self):
        return self.title


    class Meta:
        verbose_name = 'Kadr'
        verbose_name_plural = 'Kadrlar'
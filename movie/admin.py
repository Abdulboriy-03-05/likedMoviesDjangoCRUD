from django.contrib import admin
from .models import  Movie, Category
# Register your models here.
@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ["title", "id","year", "rating"]
    list_display_links = ["title"]
    list_filter = ["year", "rating"]
    prepopulated_fields = {"slug":("title",)}

admin.site.register(Category)


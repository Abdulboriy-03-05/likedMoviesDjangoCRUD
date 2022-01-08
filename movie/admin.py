from django.contrib import admin
from .models import  Movie, Category, Movie_Shots
from django.utils.html import mark_safe

class MovieShotsInline(admin.TabularInline):
    model = Movie_Shots
    extra = 2
    readonly_fields = ('get_image',)

    def get_image(self, obj):
        return mark_safe(f"<img src='{obj.image.url}' width='50' height='auto'>")

    get_image.short_description = 'Filmdan kadr'
    
# Register your models here.
@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ["title", "id","year", "rating", 'get_image']
    list_display_links = ["title"]
    list_filter = ["year", "rating"]
    list_editable = ["rating"]
    prepopulated_fields = {"slug":("title",)}
    
    inlines = [MovieShotsInline]
    
    readonly_fields = ('get_image',)
    
    def get_image(self, obj):
        return mark_safe(f"<img src='{obj.poster.url}' width='50' height='auto'>")
    
    get_image.short_description = 'Film rasmi'

admin.site.register(Category)

@admin.register(Movie_Shots)
class MovieshotsAdmin(admin.ModelAdmin):
    list_display = ('movie',)
    list_filter = ('title',)

admin.site.site_title = "Django My Movies"
admin.site.site_header = "Django My Movies"


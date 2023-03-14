from django.contrib import admin

from .models import Movie
from .models import Director

class MovieAdmin(admin.ModelAdmin):
    list_display = ['name', 'year', 'director']
    list_display_links = ['name']
    search_fields = ['name']
class DirAdmin(admin.ModelAdmin):
    list_display = ['name', 'birth_year']
    list_display_links = ['name']
    search_fields = ['name']

admin.site.register(Movie, MovieAdmin)
admin.site.register(Director, DirAdmin)
from django.contrib import admin
from .models import Movies
# Register your models here.
class Movie_Admin(admin.ModelAdmin):
    list_display= [ 'date_in_MM_DD_YY' , 'Movie_name' , 'Actress_name' , 'Actor_name' , 'rating']

admin.site.register(Movies , Movie_Admin)
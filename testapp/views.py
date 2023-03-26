from django.shortcuts import render
from .forms import Movies_form
from .models import Movies
# Create your views here.
def Homepage(request):
    form = Movies_form()
    return render(request , 'testapp/homepage.html')

def add_movie_view(request):
    form = Movies_form()
    if request.method == "POST":
        form = Movies_form(request.POST)
        if form.is_valid():
            form.save(commit=True)
            print("Movie added to database")
        return Homepage(request)
    return render(request , 'testapp/addmovie.html' , {'form':form})
            
def display_movie(request):
    movies_list = Movies.objects.all()
    return render(request , 'testapp/display.html' , {'movies': movies_list})
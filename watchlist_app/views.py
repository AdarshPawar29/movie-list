from django.shortcuts import render
from watchlist_app.models import Movie
# Create your views here.


def movie_list(request):
    movies = Movie.objects.all()
    print(movies)
    # return render(request, 'watchlist_app/movie_list.html', {'movies': movies})

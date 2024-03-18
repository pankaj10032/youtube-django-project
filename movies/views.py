from django.http import HttpResponse
from django.shortcuts import render
from .models import Movie
# def movies(request):
#     return HttpResponse("hello, there")

# def movies(request):
#     return render(request, "movies/movies.html", {"movies":["movie1","movie2"]})

# data={"movies":["movie1","movie2"]}

data={
    "movies":[
        {
            "id":5,
            "title":"jaws",
            "year":1969
        },
        {
           "id":6,
            "title":"sharkando",
            "year":1669
        }
        ,{
            "id":7,
            "title":"The mac",
            "year":2000
        }
    ]
}

def movies(request):
    data= Movie.objects.all()
    # return render(request, "movies/movies.html", data)
    return render(request, "movies/movies.html", {"movies":data})


def home(request):
    return HttpResponse("home, bye")


def detail(request, id):
    data= Movie.objects.get(pk=id)
    return render(request, 'movies/detail.html', {"movie":data})
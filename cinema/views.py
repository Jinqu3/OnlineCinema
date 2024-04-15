from django.shortcuts import render
from django.views.generic.base import View
from .models import Film,Member

class MovieView(View):

    def get(self,request):
        movies = Film.objects.all()
        return render(request,"movies/movies.html",{"movie_list": movies})


class ActorView(View):

    def get(self,request):
        actors = Member.objects.all()
        return render(request,"movies/actors_list.html",{"actors_list": actors})
    
class MovieDetail(View):

    def get(self,request,pk):
        movie = Film.objects.prefetch_related('').get(id=pk)
        return render(request,"movie/movie_single.html",{"movie":movie})
from django.shortcuts import render,redirect
from django.views.generic.base import View
from django.views.generic import ListView
from .models import Film,Member,FilmMemberPost
from .forms import ReviewForm

class MovieView(ListView):
    def get(self,request):
        movies = Film.objects.all()
        return render(request,"movies/movies.html",{"movie_list": movies})

class ActorView(View):

    def get(self,request):
        actors = Member.objects.all()
        return render(request,"movies/actors_list.html",{"actors_list": actors})
    
class MovieDetail(View):
    def get(self,request,slug):
        movie = Film.objects.get(url=slug)
        return render(request,"movies/movie_single.html",{"movie":movie})
    
class AddReview(View):
    def post(self,request,pk):
        form = request.POST
        movie = Film.objects.get(id=pk)
        if form.is_valid():
            form = form.save(commit = False)
            form.movie = movie
            form.save()
        return redirect("/")
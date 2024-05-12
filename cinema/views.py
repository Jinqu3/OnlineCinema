from typing import Any
from django.shortcuts import render,redirect,HttpResponse
from django.views.generic.base import View
from django.views.generic import ListView,DetailView
from django.db.models import Q
from .models import Film,Member,Genre,Score
from .forms import ReviewForm,RatingForm

class GenreYear:

    def get_genres(self):
        return Genre.objects.all()
    
    def get_years(self):
        return Film.objects.all().values("year")

class MovieView(GenreYear,ListView):
    model = Film
    queryset =  Film.objects.all()
    template_name = "films/film_list.html"

    # def get(self,request):
    #     movies = Film.objects.all()
    #     return render(request,"movies/movies.html",{"movie_list": movies})

class MemberView(GenreYear,DetailView):
    
    model = Member
    template_name = "films/member_detail.html"
    slug_field = "url"   
    
    #  def get(self,request,slug):
    #     member = Member.objects.get(url=slug)
    #     return render(request,"movies/member_single.html",{"member":member})
    
class MovieDetailView(GenreYear,DetailView):

    model = Film
    template_name = "films/film_detail.html"
    slug_field = "url"

    def get_context_data(self, **kwargs: Any):
        context =  super().get_context_data(**kwargs)
        context['star_form'] = RatingForm()
        return context



    # def get(self,request,slug):
    #     movie = Film.objects.get(url=slug)
    #     return render(request,"movies/movie_single.html",{"movie":movie})

class AddReviewView(View):

    template_name = "films/film_detail.html"

    def post(self,request,pk):
        form = ReviewForm(request.POST)
        if form.is_valid():
            form = form.save(commit = False)
            form.film_id = pk
            form.save()
        return redirect("/")    
    
class FilterMovieView(GenreYear, ListView):

    template_name = "films/film_list.html"

    def get_queryset(self):
        queryset = Film.objects.filter(
            Q(year__in=self.request.GET.getlist("year")) |
            Q(genres__in=self.request.GET.getlist("genre"))
        ).distinct()
        return queryset

class AddStarRating(View):
    """Добавление рейтинга фильму"""

    def get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip

    def post(self, request):
        form = RatingForm(request.POST)
        if form.is_valid():
            Score.objects.update_or_create(
                user_id=self.get_client_ip(request),
                film_id=int(request.POST.get("film")),
                defaults={'star': int(request.POST.get("star"))}
            )
            return HttpResponse(status=201)
        else:
            return HttpResponse(status=400)
        


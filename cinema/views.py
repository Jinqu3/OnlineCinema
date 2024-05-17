from typing import Any
from django.shortcuts import render,redirect,HttpResponse
from django.views.generic.base import View
from django.views.generic import ListView,DetailView
from django.db.models import Q
from .models import Film,Member,Genre,Score,User,ScoreStar
from .forms import ReviewForm,RatingForm, FavoriteForm, ViewedForm
from django.shortcuts import get_object_or_404

class GenreYear:

    def get_genres(self):
        return Genre.objects.all()
    
    def get_years(self):
        return Film.objects.all().values("year")
    
    def get_stars(self):
        return ScoreStar.objects.all().values("value")
    
    def get_rating(self):
        return Film.objects.all().values("rating")
    
    def get_mpaa_rating(self):
        return Film.objects.all().values("mpaa_rating")

class MovieView(GenreYear,ListView):
    model = Film
    queryset =  Film.objects.all().order_by('id')
    template_name = "films/film_list.html"
    paginate_by = 6

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
    queryset = Film.objects.all().prefetch_related()

    def get_context_data(self, **kwargs: Any):
        context =  super().get_context_data(**kwargs)
        context['star_form'] = RatingForm()
        return context



    # def get(self,request,slug):
    #     movie = Film.objects.get(url=slug)
    #     return render(request,"movies/movie_single.html",{"movie":movie})

    
class FilterMovieView(GenreYear, ListView):

    template_name = "films/film_list.html"
    paginate_by = 1

    def get_queryset(self):
        queryset = Film.objects.filter(
            Q(year__in=self.request.GET.getlist("year")) |
            Q(genres__in=self.request.GET.getlist("genre"))|
            Q(rating__in=self.request.GET.getlist("rating")) |
            Q(mpaa_rating__in=self.request.GET.getlist("mpaa_rating"))
        ).distinct()
        return queryset
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["year"] = ''.join([f"year={x}&" for x in self.request.GET.getlist("year")])
        context["genre"] = ''.join([f"genre={x}&" for x in self.request.GET.getlist("genre")])
        context["rating"] = ''.join([f"rating={x}&" for x in self.request.GET.getlist("rating")])
        context["mpaa_rating"] = ''.join([f"mpaa_rating={x}&" for x in self.request.GET.getlist("mpaa_rating")])
        return context


class AddToFavoriteView(View):
    template_name = "films/film_detail.html"

    def post(self, request, film_id):
        film = get_object_or_404(Film, id=film_id)
        form = FavoriteForm(request.POST or None) 
        user = User.objects.get(user=request.user)  
        if form.is_valid():
            if film in user.favorite.all():
                user.favorite.remove(film)
            else:
                user.favorite.add(film)
        return redirect(film.get_absolute_url())

class MarkAsViewedView(View):
    template_name = "films/film_detail.html"

    def post(self, request, film_id):
        film = get_object_or_404(Film, id=film_id)
        form = ViewedForm(request.POST or None)
        user = User.objects.get(user=request.user)
        if form.is_valid():
            if film in user.views.all():
                user.views.remove(film)
            else:
                user.views.add(film)
        return redirect(film.get_absolute_url())
    
class AddStarRating(View):
    """Добавление рейтинга фильму"""

    template_name = "films/film_detail.html"

    def post(self, request, slug):
        form = RatingForm(request.POST)
        film = get_object_or_404(Film, url=slug)

        if form.is_valid():
            if request.user.is_authenticated:
                user = User.objects.get(user=request.user)
                Score.objects.update_or_create(
                    user=user,
                    film=film,
                    defaults={'star': form.cleaned_data['star']}
                )
        return redirect(film.get_absolute_url()) 
    
class AddReviewView(View):

    template_name = "films/film_detail.html"

    def post(self,request,slug):
        form = ReviewForm(request.POST)
        film = get_object_or_404(Film,id=slug)
        if form.is_valid():
            if request.user.is_authenticated:
                form = form.save(commit = False)
                form.film = film
                if request.user.is_authenticated:
                    form.user = User.objects.get(user=request.user)
                form.save()
        return redirect(film.get_absolute_url())    
        
class Search(ListView):
    """Поиск фильмов"""
    template_name = "films/film_list.html"

    def get_queryset(self):
        return Film.objects.filter(name__icontains=self.request.GET.get("q"))

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["q"] = f'q={self.request.GET.get("q")}&'
        return context
    
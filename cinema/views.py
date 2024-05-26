from typing import Any
from django.shortcuts import render,redirect,HttpResponse
from django.views.generic.base import View
from django.views.generic import ListView,DetailView
from django.db.models import Q
from .models import Film,Member,Genre,Score,User,ScoreStar,Review,Country
from .forms import ReviewForm,RatingForm, FavoriteForm, ViewedForm
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required


from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, Table, TableStyle
from io import BytesIO
from django.http import HttpResponse
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle

from django.db.models import Q, Func, F, DecimalField
from django.db.models.functions import Round

class GenreYear:

    def get_genres(self):
        return Genre.objects.all()
    
    def get_years(self):
        return Film.objects.all().values("year")
    
    def get_stars(self):
        return ScoreStar.objects.all().values("value")
    
    def get_ages(self):
        return Film.objects.all().values("age")
    
    def get_mpaa_rating(self):
        return Film.objects.all().values("mpaa_rating")
    
    def get_countries(self):
        return Country.objects.all()

class MovieView(GenreYear,ListView):
    model = Film
    queryset =  Film.objects.all().order_by('id')
    template_name = "films/film_list.html"
    paginate_by = 6

class MemberView(GenreYear,DetailView):
    
    model = Member
    template_name = "films/member_detail.html"
    slug_field = "url"

    
class MovieDetailView(GenreYear,DetailView):

    model = Film
    template_name = "films/film_detail.html"
    slug_field = "url"
    queryset = Film.objects.all().select_related()

    def get_context_data(self, **kwargs: Any):
        context =  super().get_context_data(**kwargs)
        context['star_form'] = RatingForm()

        if self.request.user.is_authenticated:

            user = User.objects.get(user=self.request.user) 
            context['user'] = user

    
        return context

class FilterMovieView(GenreYear, ListView):

    template_name = "films/film_list.html"
    paginate_by = 1

    def get_queryset(self):
        queryset = Film.objects.annotate(
                rounded_rating=Round('rating', 0, output_field=DecimalField())
            ).filter(
            Q(year__in=self.request.GET.getlist("year")) if self.request.GET.getlist("year") else Q(),
            Q(genres__in=self.request.GET.getlist("genre")) if self.request.GET.getlist("genre") else Q(),
            Q(rounded_rating__in=self.request.GET.getlist("star")) if self.request.GET.getlist("star") else Q(),
            Q(mpaa_rating__in=self.request.GET.getlist("mpaa_rating")) if self.request.GET.getlist("mpaa_rating") else Q(),
            Q(countries__in=self.request.GET.getlist("country")) if self.request.GET.getlist("country") else Q()
        ).distinct()


        return queryset
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["year"] = ''.join([f"year={x}&" for x in self.request.GET.getlist("year")])
        context["genre"] = ''.join([f"genre={x}&" for x in self.request.GET.getlist("genre")])
        context["rating"] = ''.join([f"rating={x}&" for x in self.request.GET.getlist("star")])
        context["mpaa_rating"] = ''.join([f"mpaa_rating={x}&" for x in self.request.GET.getlist("mpaa_rating")])
        context["country"] = ''.join([f"country={x}&" for x in self.request.GET.getlist("country")])

        return context



class AddToFavoriteView(View):
    template_name = "films/film_detail.html"

    def post(self, request, film_id):
        film = get_object_or_404(Film, id=film_id)
        form = FavoriteForm(request.POST or None) 
        user = User.objects.get(user=request.user)  
        if form.is_valid():
            if request.user.is_authenticated:
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
            if request.user.is_authenticated:
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
                film.rating = film.get_average_rating()
                film.save()
        return redirect(film.get_absolute_url()) 
    
class AddReviewView(View):
    template_name = "films/film_detail.html"  # Убедитесь, что это имя вашего шаблона

    def post(self, request, slug):
        film = get_object_or_404(Film, id=slug)  # Исправлено: поиск фильма по slug
        if request.user.is_authenticated:
            if 'submit_review' in request.POST:
                form = ReviewForm(request.POST)
                if form.is_valid():
                    review = form.save(commit=False)
                    review.film = film
                    review.user = request.user.user  # Используем related_name "user"
                    review.save()
            elif 'delete_review' in request.POST:
                review_id = request.POST.get('delete_review')
                review = get_object_or_404(Review, review_id=review_id)
                review.delete()

        return redirect(film.get_absolute_url())

    def get(self, request, slug):
        film = get_object_or_404(Film, id=slug) 
        reviews = film.review_set.all()
        form = ReviewForm()
        context = {'film': film, 'reviews': reviews, 'form': form}
        return render(request, self.template_name, context)
    
class Search(ListView):
    """Поиск фильмов"""
    template_name = "films/film_list.html"

    def get_queryset(self):
        return Film.objects.filter(name__icontains=self.request.GET.get("q"))

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["q"] = f'q={self.request.GET.get("q")}&'
        return context

@login_required
def generate_film_pdf_report(request, film_id):

    pdfmetrics.registerFont(TTFont('MyFont', 'static/font.ttf'))
    
    try:
        film = Film.objects.get(id=film_id)
    except Film.DoesNotExist:
        return HttpResponse("Film does not exist.")
    
    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=A4)
    elements = []
    
     # Set up styles
    styles = getSampleStyleSheet()
    
    # Define custom styles with the custom font
    normal_style = ParagraphStyle(
        'Normal',
        parent=styles['Normal'],
        fontName='MyFont',
        fontSize=12
    )
    
    heading_style = ParagraphStyle(
        'Heading2',
        parent=styles['Heading2'],
        fontName='MyFont',
        fontSize=18
    )

    # Title
    title = Paragraph(f"{film.name} ({film.year})", heading_style)
    elements.append(title)
    
    # Film details
    details = [
        f"Год: {film.year}",
        f"Страна: {', '.join(country.name for country in film.countries.all())}",
        f"Слоган: {film.slogan}",
        # f"Director: {', '.join([f'<a href="{member.get_absolute_url}">{member.name} {member.surname} {member.last_name}</a>' for member in film.filmmemberpost_set.filter(post__name__in=['Director', 'Режиссёр'])])}",
        # f"Operator: {', '.join([f'<a href="{member.get_absolute_url}">{member.name} {member.surname} {member.last_name}</a>' for member in film.filmmemberpost_set.filter(post__name__in=['Operator', 'Оператор'])])}",
        # f"Scenario: {', '.join([f'<a href="{member.get_absolute_url}">{member.name} {member.surname} {member.last_name}</a>' for member in film.filmmemberpost_set.filter(post__name__in=['Scenarist', 'Сценарист'])])}",
        # f"Compositor: {', '.join([f'<a href="{member.get_absolute_url}">{member.name} {member.surname} {member.last_name}</a>' for member in film.filmmemberpost_set.filter(post__name__in=['Compositor', 'Композитор'])])}",
        # f"Actor: {', '.join([f'<a href="{member.get_absolute_url}">{member.name} {member.surname} {member.last_name}</a>' for member in film.filmmemberpost_set.filter(post__name__in=['Actor', 'Актёр'])])}",
        f"Жанры: {', '.join(genre.name for genre in film.genres.all())}",
        f"Дата выхода (Мир): {film.release_date_world}",
        f"Дата выхода (Россия): {film.release_date_russia}",
        f"Бюджет: {film.budjet} $",
        f"Кассовый сбор: {film.gross} $",
        f"Рейтинг: {film.get_average_rating()}",
        f"Количество отзывов: {film.get_review_count()}",  
        f"Количество оценок: {film.get_score_count()}",    
        f"Добавлено в избранное: {film.get_favorites_count()}",  
        f"Просмотрено: {film.get_watched_count()}",
    ]

    for detail in details:
        elements.append(Paragraph(detail, normal_style))
    
    elements.append(Paragraph(f"О фильме {film.name}",heading_style))
    elements.append(Paragraph(film.description, normal_style))

    doc.build(elements)
    buffer.seek(0)
    return HttpResponse(buffer.getvalue(), content_type='application/pdf')
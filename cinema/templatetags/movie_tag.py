from django import template
from cinema.models import Film

register = template.Library()

@register.inclusion_tag('movies/tags/last_movies.html')
def get_last_movies(count=5):
    movies = Film.objects.order_by("id")[:count]
    return {"last_movies":movies}
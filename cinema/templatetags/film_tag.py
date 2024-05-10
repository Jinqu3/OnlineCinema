from django import template
from cinema.models import Film

register = template.Library()

@register.inclusion_tag('films/tags/last_films.html')
def get_last_movies(count=5):
    films = Film.objects.order_by("id")[:count]
    return {"last_films":films}
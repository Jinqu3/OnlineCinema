from django import template
from cinema.models import Film

register = template.Library()

@register.inclusion_tag('films/tags/last_films.html')
def get_last_movies(count=5):
    films = Film.objects.order_by("id")[:count]
    return {"last_films":films}

@register.filter(name='add_class')
def add_class(field, css_class):
    return field.as_widget(attrs={'class': css_class})

@register.filter
def get_favorite(user):
    return user.get_favorite()
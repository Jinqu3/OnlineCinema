from modeltranslation.translator import register, TranslationOptions
from .models import Category, Member,Film, Genre, Photo,Country,Post


@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name', 'description')

@register(Country)
class CountryTranslationOptions(TranslationOptions):
    fields = ('name',)

@register(Member)
class MemberTranslationOptions(TranslationOptions):
    fields = ('name','surname','lastname','gender')


@register(Genre)
class GenreTranslationOptions(TranslationOptions):
    fields = ('name',)

@register(Post)
class PostTranslationOptions(TranslationOptions):
    fields = ('name',)


@register(Film)
class FilmTranslationOptions(TranslationOptions):
    fields = ('name', 'slogan')


@register(Photo)
class PhotoTranslationOptions(TranslationOptions):
    fields = ('name', 'description')
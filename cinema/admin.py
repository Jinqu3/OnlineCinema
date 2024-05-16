from django.contrib import admin

from .models import Film,Genre,Category,Country,Photo,Member,FilmMemberPost,Review,Score,User,Post,ScoreStar
from modeltranslation.admin import TranslationAdmin
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms

from django.utils.safestring import mark_safe



class FilmUserReviewInline(admin.TabularInline):
    model = Review
    fk_key = "user"
    extra = 1

class FilmUserScoreInline(admin.TabularInline):
    model = Score
    extra = 1

@admin.register(User)
class FilmUserAdmin(admin.ModelAdmin):
    inlines = [
        FilmUserReviewInline,
        FilmUserScoreInline,
    ]
    

admin.register(User,FilmUserAdmin)

@admin.register(ScoreStar)
class ScoreAdmin(admin.ModelAdmin):
    """Отзывы к фильму"""
    list_display = ("value",)

@admin.register(Post)
class ReviewAdmin(TranslationAdmin):
    """Отзывы к фильму"""
    list_display = ("name",)
    fk_name = "user"

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    """Отзывы к фильму"""
    list_display = ("film", "user")

@admin.register(Country)
class GenreAdmin(TranslationAdmin):
    """Жанры"""
    list_display = ("name",)

@admin.register(Category)
class CategoryAdmin(TranslationAdmin):
    """Категории"""
    list_display = ("name", "description")
    list_display_links = ("name",)

@admin.register(Genre)
class GenreAdmin(TranslationAdmin):
    """Жанры"""
    list_display = ("name", "description")
    list_display_links = ("name",)

@admin.register(Score)
class RatingAdmin(admin.ModelAdmin):
    """Рейтинг"""
    list_display = ("user", "film", "star")

@admin.register(Member)
class MemberAdmin(TranslationAdmin):
    list_display = ("name","surname","lastname", "date_of_birth", "get_image")
    readonly_fields = ("get_image",)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.photo.url} width="50" height="60"')

    get_image.short_description = "Изображение"

@admin.register(Photo)
class MovieShotsAdmin(TranslationAdmin):
    """Кадры из фильма"""
    list_display = ("name", "film_id", "get_image")
    readonly_fields = ("get_image",)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="50" height="60"')

    get_image.short_description = "Изображение"

class ReviewInline(admin.TabularInline):
    """Отзывы на странице фильма"""
    model = Review
    extra = 1

class MovieShotsInline(admin.TabularInline):
    model = Photo
    extra = 1
    
    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="100" height="110"')

    get_image.short_description = "Изображение"

class FilmMemberPostInline(admin.TabularInline):
    model = FilmMemberPost
    extra = 1

@admin.register(Film)
class FilmAdmin(TranslationAdmin):
    """Фильмы"""
    list_display = ("name",)
    list_filter = ("year",)
    inlines = [MovieShotsInline, ReviewInline,FilmMemberPostInline]
    save_on_top = True
    save_as = True
    readonly_fields = ("get_image",)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.poster.url} width="100" height="110"')

    get_image.short_description = "Постер"


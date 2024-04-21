from django.contrib import admin

from .models import Film,Genre,Category,Country,Photo,Member,FilmMemberPost,Review,Score,User,Post

from ckeditor_uploader.widgets import CKEditorUploadingWidget

from django import forms

from django.utils.safestring import mark_safe


class FilmAdminForm(forms.ModelForm):
    description = forms.CharField(label="Описание",widget = CKEditorUploadingWidget())

    class Meta:
        model = Film
        fields = '__all__'


class FilmMemberPostInline(admin.TabularInline):
    model = FilmMemberPost
    extra = 1

class FilmUserReviewInline(admin.TabularInline):
    model = Review
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
admin.site.register(Genre)
admin.site.register(Category)
admin.site.register(Country)
admin.site.register(Photo)
admin.site.register(Member)
admin.site.register(Post)
admin.site.register(Review)


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

@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):
    """Фильмы"""
    list_display = ("name",)
    list_filter = ("year",)
    search_fields = ("title", "category__name")
    inlines = [MovieShotsInline, ReviewInline,FilmMemberPostInline]
    save_on_top = True
    save_as = True
    form = FilmAdminForm
    readonly_fields = ("get_image",)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.poster.url} width="100" height="110"')

    get_image.short_description = "Постер"


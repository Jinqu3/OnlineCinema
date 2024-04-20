from django.contrib import admin

from .models import Film,Genre,Category,Country,Photo,Member,FilmMemberPost,Review,Score,User,Post


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

@admin.register(Film)
class FilmMemberPostAdmin(admin.ModelAdmin):
    inlines = [
        FilmMemberPostInline,
    ]

admin.register(Film,FilmMemberPostAdmin)
admin.register(User,FilmUserAdmin)
admin.site.register(Genre)
admin.site.register(Category)
admin.site.register(Country)
admin.site.register(Photo)
admin.site.register(Member)
admin.site.register(Post)

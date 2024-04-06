from django.contrib import admin

from .models import Film,Genre,Category,Country,Photo,Member,Post

admin.site.register(Film)
admin.site.register(Genre)
admin.site.register(Category)
admin.site.register(Country)
admin.site.register(Photo)
admin.site.register(Member)
admin.site.register(Post)
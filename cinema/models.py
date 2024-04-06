from django.db import models



"""
Пользователь
"""
class User(models.Model):
    MALE = 'M'
    FEMALE = 'F'
    GENDERS = [
        (MALE,'Мужчина'),
        (FEMALE,'Женщина')
    ]

    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30, blank=True, null=True)
    date_of_birth = models.DateField()
    gedner = models.CharField(max_length=1,choices=GENDERS)
    login = models.CharField(max_length=30)
    password = models.CharField(max_length=100)
    email = models.CharField(max_length=256)
    photo = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = True
        db_table = '_user'

class Role(models.Model):
    name = models.CharField(max_length=20)

    class Meta:
        managed = True
        db_table = 'role'

class UserRole(models.Model):
    user = models.ForeignKey(User,on_delete= models.CASCADE) 
    role = models.ForeignKey(Role, on_delete= models.CASCADE)

    class Meta:
        managed = True
        db_table = 'user_role'
        unique_together = (('user', 'role'),)

"""
Фильм
"""
class Film(models.Model):
    name = models.CharField(max_length=130)
    slogan = models.CharField(max_length=50, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    poster = models.CharField(max_length=100, blank=True, null=True)
    release_date_world = models.DateField(blank=True, null=True)
    release_date_russia = models.DateField(blank=True, null=True)
    budjet = models.IntegerField(blank=True, null=True)
    gross = models.IntegerField(blank=True, null=True)
    duration = models.DateTimeField(blank=True, null=True)
    reating = models.DecimalField(max_digits=1, decimal_places=1, blank=True, null=True)
    mpaa_rating = models.CharField(max_length=5, blank=True, null=True)
    url = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'film'

"""
Категория
"""
class Category(models.Model):
    name = models.CharField(max_length=30, blank=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'category'

class FilmCategory(models.Model):
    film = models.ForeignKey(Film, on_delete= models.CASCADE)  # The composite primary key (film_id, category_id) found, that is not supported. The first column is selected.
    category = models.ForeignKey(Category, on_delete= models.CASCADE)

    class Meta:
        managed = False
        db_table = 'film_category'
        unique_together = (('film', 'category'),)
"""
Страна
"""
class Country(models.Model):
    name = models.CharField(max_length=56)

    class Meta:
        managed = False
        db_table = 'country'

class FilmCountry(models.Model):
    film = models.ForeignKey(Film, on_delete= models.CASCADE)  # The composite primary key (film_id, country_id) found, that is not supported. The first column is selected.
    country = models.ForeignKey(Country, on_delete= models.CASCADE)

    class Meta:
        managed = False
        db_table = 'film_country'
        unique_together = (('film', 'country'),)
"""
Жанр
"""
class Genre(models.Model):
    name = models.CharField(max_length=40)
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'genre'

class FilmGenre(models.Model):
    film = models.ForeignKey(Film, on_delete= models.CASCADE) 
    genre = models.ForeignKey('Genre', on_delete= models.CASCADE)

    class Meta:
        managed = False
        db_table = 'film_genre'
        unique_together = (('film', 'genre'),)

"""
Съёмочная группа
"""
class Member(models.Model):
    MALE = 'M'
    FEMALE = 'F'
    GENDERS = [
        (MALE,'Мужчина'),
        (FEMALE,'Женщина')
    ]

    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=30)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=1,choices=GENDERS)
    photo = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'member'

"""
Фото
"""
class Photo(models.Model):
    name = models.CharField(max_length=40)
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'photo'

class FilmPhoto(models.Model):
    film = models.OneToOneField(Film, on_delete= models.CASCADE)
    photo = models.ForeignKey(Photo, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'film_photo'
        unique_together = (('film', 'photo'),)

"""
Должность участника съёмочной группы
"""
class Post(models.Model):
    name = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'post'

"""Вообще"""
class MemberPost(models.Model):
    member = models.ForeignKey(Member, on_delete= models.CASCADE)
    post = models.ForeignKey('Post', on_delete= models.CASCADE)

    class Meta:
        managed = False
        db_table = 'member_post'
        unique_together = (('member', 'post'),)

"""В фильме"""
class FilmMemberPost(models.Model):
    film = models.ForeignKey(Film, on_delete= models.CASCADE)  
    member = models.ForeignKey('Member',on_delete= models.CASCADE)
    post = models.ForeignKey('Post', on_delete= models.CASCADE)

    class Meta:
        managed = False
        db_table = 'film_member_post'
        unique_together = (('film', 'member', 'post'),)

"""
Избранное
"""
class Favorite(models.Model):
    film = models.OneToOneField('Film', on_delete= models.CASCADE, primary_key=True)  # The composite primary key (film_id, user_id) found, that is not supported. The first column is selected.
    user = models.ForeignKey(User, on_delete= models.CASCADE)

    class Meta:
        managed = False
        db_table = 'favorite'
        unique_together = (('film', 'user'),)

"""
Отзыв
"""
class Review(models.Model):
    review_id = models.AutoField(primary_key=True)  
    film = models.ForeignKey(Film,on_delete= models.CASCADE)
    user = models.ForeignKey(User,on_delete= models.CASCADE)
    text = models.TextField(max_length=5000)

    class Meta:
        managed = False
        db_table = 'review'
        unique_together = (('film', 'user'),)

"""
Оценка
"""
class Score(models.Model):
    film = models.ForeignKey(Film, on_delete= models.CASCADE)
    user = models.ForeignKey(User,on_delete= models.CASCADE)
    star = models.DecimalField(max_digits=2, decimal_places=0)

    class Meta:
        managed = False
        db_table = 'score'
        unique_together = (('film', 'user'),)

"""
Просмотренное
"""
class Viewed(models.Model):
    film = models.ForeignKey(Film, on_delete= models.CASCADE)
    user = models.ForeignKey(User,on_delete= models.CASCADE)

    class Meta:
        managed = False
        db_table = 'viewed'
        unique_together = (('film', 'user'),)

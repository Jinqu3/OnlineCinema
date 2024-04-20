from django.db import models
from datetime import datetime
from django.urls import reverse

"""
Пользователь
""" 
class Role(models.Model):
    name = models.CharField(max_length=20)

    class Meta:

        verbose_name = "Роль"
        verbose_name_plural = "Роли"

        managed = True
        db_table = 'role'
        
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
    gender = models.CharField(max_length=1,choices=GENDERS)
    login = models.CharField(max_length=30)
    password = models.CharField(max_length=100)
    email = models.CharField(max_length=256)
    photo = models.ImageField(upload_to="users/")

    roles = models.ManyToManyField("Role")
    views = models.ManyToManyField("Film",related_name="viewed")
    favorite = models.ManyToManyField("Film",related_name="favorite")
    scores = models.ManyToManyField("Film",through="Score",related_name="scores")

    def __str__(self):
        return self.name+self.surname

    class Meta:

        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

        managed = True
        db_table = '_user'

"""
Категория
"""
class Category(models.Model):
    name = models.CharField(max_length=30, blank=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:

        verbose_name = "Категория"
        verbose_name_plural = "Категории"

        managed = True
        db_table = 'category'


"""
Страна
"""
class Country(models.Model):
    name = models.CharField(max_length=56,unique=True)

    def __str__(self):
        return self.name
    
    class Meta:

        verbose_name = "Страна"
        verbose_name_plural = "Страны"

        managed = True
        db_table = 'country'

"""
Жанр
"""
class Genre(models.Model):
    name = models.CharField(max_length=40,unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
    
    class Meta:

        verbose_name = "Жанр"
        verbose_name_plural = "Жанры"

        managed = True
        db_table = 'genre'


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
    last_name = models.CharField(max_length=30,blank=True)
    description = models.TextField(max_length=1000,blank=True, null=True)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=1,choices=GENDERS)
    photo = models.ImageField(upload_to="members/",null=True)

    def __str__(self):
        return self.name + " " + self.surname + " " +self.last_name


    class Meta:

        verbose_name = "Участник"
        verbose_name_plural = "Участники"

        managed = True
        db_table = 'member'
        unique_together = (('name', 'surname'),)

"""
Фото
"""
class Photo(models.Model):
    name = models.CharField(max_length=40)
    film_id = models.ForeignKey("Film",on_delete=models.CASCADE,null=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to=f"photo/",null=True)

    class Meta:

        verbose_name = "Фото"
        verbose_name_plural = "Фотографии"

        managed = True
        db_table = 'photo'
"""
Фильм
"""
class Film(models.Model):

    YEAR_CHOICES = []
    for r in range(1980, (datetime.now().year+1)):
        YEAR_CHOICES.append((r,r))

    name = models.CharField(max_length=130,unique=True)
    slogan = models.CharField(max_length=50, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    poster = models.ImageField(upload_to="films/",null=True)
    year = models.IntegerField(choices=YEAR_CHOICES, default=datetime.now().year)
    release_date_world = models.DateField(blank=True, null=True)
    release_date_russia = models.DateField(blank=True, null=True)
    budjet = models.IntegerField(blank=True, null=True)
    gross = models.IntegerField(blank=True, null=True)
    duration = models.CharField(max_length=3,blank=True, null=True)
    rating = models.CharField(max_length=3,blank=True, null=True)
    mpaa_rating = models.CharField(max_length=5, blank=True, null=True)
    trailer_url = models.CharField(max_length=256, blank=True, null=True)
    url = models.SlugField(max_length=256,unique=True, blank=True, null=True)

    countries = models.ManyToManyField("Country",related_name="film_countries")
    genres = models.ManyToManyField("Genre",related_name="film_genres")
    categories = models.ManyToManyField("Category",related_name="film_categories")
    members = models.ManyToManyField("Member",through="FilmMemberPost",related_name="film_members")
    members_posts = models.ManyToManyField("Post",through="FilmMemberPost",related_name="film_member_posts")

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("movie_detail", kwargs = {"slug":self.url})

    class Meta:

        verbose_name = "Фильм"
        verbose_name_plural = "Фильмы"

        managed = True
        db_table = 'film'

class FilmMemberPost(models.Model):
    film = models.ForeignKey('Film', on_delete= models.CASCADE)  
    member = models.ForeignKey('Member',on_delete= models.CASCADE)
    post = models.ForeignKey('Post', on_delete= models.CASCADE)

    class Meta:
        managed = True
        db_table = 'film_member_post'
        unique_together = (('film', 'member', 'post'),)

"""
Должность участника съёмочной группы
"""
class Post(models.Model):
    name = models.CharField(max_length=20,unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Должность"
        verbose_name_plural = "Должности"

        managed = True
        db_table = 'post'   

"""
Отзыв
"""
class Review(models.Model):
    review_id = models.AutoField(primary_key=True)  
    film = models.ForeignKey("Film",on_delete= models.CASCADE)
    user = models.ForeignKey("User",on_delete= models.CASCADE)
    text = models.TextField(max_length=5000)

    class Meta:

        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"

        managed = True
        db_table = 'review'
        unique_together = (('film', 'user'),)

"""
Оценка
"""
class Score(models.Model):
    film = models.ForeignKey("Film", on_delete= models.CASCADE)
    user = models.ForeignKey("User",on_delete= models.CASCADE)
    star = models.DecimalField(max_digits=2, decimal_places=0)
    

    class Meta:

        verbose_name = "Оцененка"
        verbose_name_plural = "Оценки"

        managed = True
        db_table = 'score'
        unique_together = (('film', 'user'),)

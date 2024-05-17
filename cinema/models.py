from django.db import models
from datetime import datetime
from django.urls import reverse
from django.contrib.auth.models import User as DefaultUser
from django.core.validators import FileExtensionValidator
from django.db.models import Avg
from django_ckeditor_5.fields import CKEditor5Field
"""
Пользователь
""" 
class User(models.Model):

    MALE = 'Mужчина'
    FEMALE = 'Женщина'
    MALE_EN = ''
    FEMALE_EN = 'Женщина'
    GENDERS = [
        (MALE,'Мужчина'),
        (FEMALE,'Женщина'),
        (MALE_EN,'Man'),
        (FEMALE_EN,'Woman')
    ]

    user=models.OneToOneField(DefaultUser, on_delete=models.CASCADE,null = True)
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30, blank=True, null=True)
    date_of_birth = models.DateField(null=True,blank=True)
    gender = models.CharField(max_length=7,null=True,blank=True,choices=GENDERS)
    login = models.CharField(unique=True, max_length=30)
    password = models.CharField(max_length=100)
    email = models.CharField(unique=True,blank= True,max_length=256)
    photo = models.ImageField(null=True,blank=True,upload_to="users/",default="users/default_user_image.jpeg")

    views = models.ManyToManyField("Film",related_name="viewed",blank=True)
    favorite = models.ManyToManyField("Film",related_name="favorite",blank=True)
    scores = models.ManyToManyField("Film",through="Score",related_name="scores",blank=True)
    reviews = models.ManyToManyField("Film",through="Review",related_name="user_reviews",blank=True)

    def __str__(self):
        return self.name+" "+self.surname

    def get_views(self):
        return self.views.all()
    
    def get_favorite(self):
        return self.favorite.all()

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
    MALE = 'Mужчина'
    FEMALE = 'Женщина'
    MALE_EN = ''
    FEMALE_EN = 'Женщина'
    GENDERS = [
        (MALE,'Мужчина'),
        (FEMALE,'Женщина'),
        (MALE_EN,'Man'),
        (FEMALE_EN,'Woman')
    ]

    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30,blank=True)
    description = CKEditor5Field(max_length=1000,blank=True, null=True,config_name='extends')
    date_of_birth = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=7,choices=GENDERS)
    photo = models.ImageField(upload_to="members/",default="members/default_member_image.jpeg",null=True,blank = True)
    url = models.SlugField(max_length=256,unique=True, blank=False, null=True)

    members_posts = models.ManyToManyField("Post",through="FilmMemberPost",related_name="posts")

    def __str__(self):
        return self.name + " " + self.surname + " " +self.lastname
    
    def get_absolute_url(self):
        return reverse("member_detail", kwargs = {"slug":self.url})


    class Meta:

        verbose_name = "Участник"
        verbose_name_plural = "Участники"

        ordering = ['-id']
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
    description = CKEditor5Field(blank=True, null=True,config_name='extends')
    poster = models.ImageField(upload_to="films/",default="films/default_film_image.jpg",blank=True,null=True)
    year = models.IntegerField(choices=YEAR_CHOICES, blank=True,null=True)
    release_date_world = models.DateField(blank=True, null=True)
    release_date_russia = models.DateField(blank=True, null=True)
    budjet = models.IntegerField(blank=True, null=True)
    gross = models.IntegerField(blank=True, null=True)
    duration = models.CharField(max_length=3,blank=True, null=True)
    rating = models.CharField(max_length=3,blank=True, null=True)
    mpaa_rating = models.CharField(max_length=5, blank=True, null=True)
    trailer_url = models.CharField(max_length=256, blank=True, null=True)
    url = models.SlugField(max_length=256,unique=True, blank=False, null=True)
    video = models.FileField(upload_to='video/',validators = [FileExtensionValidator(allowed_extensions=['mp4'])],blank=True,null=True)  


    countries = models.ManyToManyField("Country",related_name="film_countries")
    genres = models.ManyToManyField("Genre",related_name="film_genres")
    categories = models.ManyToManyField("Category",related_name="film_categories")
    members = models.ManyToManyField("Member",through="FilmMemberPost",related_name="film_members")
    members_posts = models.ManyToManyField("Post",through="FilmMemberPost",related_name="film_member_posts")
    reviews = models.ManyToManyField("User",through="Review",related_name="film_reviews")
    user_scores = models.ManyToManyField("User",through="Score",related_name="film_scores",blank=True)
    user_views = models.ManyToManyField("User",related_name="film_viewed",blank=True)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("film_detail", kwargs = {"slug":self.url})
    
    def get_review(self):
        return self.review_set.all()
    
    def get_video(self):
        return self.video
    
    def get_user_score(self,user):
        return self.user_scores.filter(user=user)

    def get_average_rating(self):
        average_rating = self.score_set.aggregate(Avg('star__value')).get('star__value__avg')
        if average_rating is not None:
            return round(average_rating, 1)  # Округление до одного знака после запятой
        return 0 
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
    user = models.ForeignKey("User",on_delete= models.CASCADE,related_name="user_review")
    text = models.TextField(max_length=5000)

    class Meta:

        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"

        managed = True
        db_table = 'review'

"""
Оценка
"""

class ScoreStar(models.Model):

    STARS = [(i,i) for i in range(1,6)]

    value = models.IntegerField(choices=STARS,default=0)

    class Meta:
        verbose_name = "Звезда оценки"
        verbose_name_plural = "Звезды"
        ordering = ["-value"]

class Score(models.Model):
    film = models.ForeignKey("Film", on_delete= models.CASCADE)
    user = models.ForeignKey("User",on_delete= models.CASCADE)
    star = models.ForeignKey("ScoreStar",on_delete= models.CASCADE)
    

    class Meta:

        verbose_name = "Оценка"
        verbose_name_plural = "Оценки"

        managed = True
        db_table = 'score'
        unique_together = (('film', 'user'),)

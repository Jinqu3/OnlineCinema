from django.db import models

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
    photo = models.ImageField(upload_to="media/members/",null=True)

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
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to="media/photo/",null=True)

    class Meta:

        verbose_name = "Фото"
        verbose_name_plural = "Фотографии"

        managed = True
        db_table = 'photo'
"""
Фильм
"""
class Film(models.Model):

    name = models.CharField(max_length=130,unique=True)
    slogan = models.CharField(max_length=50, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    poster = models.ImageField(upload_to="media/actors/",null=True)
    year = models.DateField(blank=True, null=True)
    release_date_world = models.DateField(blank=True, null=True)
    release_date_russia = models.DateField(blank=True, null=True)
    budjet = models.IntegerField(blank=True, null=True)
    gross = models.IntegerField(blank=True, null=True)
    duration = models.DateTimeField(blank=True, null=True)
    raiting = models.DecimalField(max_digits=1, decimal_places=1, blank=True, null=True)
    mpaa_rating = models.CharField(max_length=5, blank=True, null=True)
    trailer_url = models.CharField(max_length=256, blank=True, null=True)
    url = models.CharField(max_length=256, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:

        verbose_name = "Фильм"
        verbose_name_plural = "Фильмы"

        managed = True
        db_table = 'film'

"""
Связи многие ко многим
"""
class UserRole(models.Model):
    user = models.ForeignKey(User,on_delete= models.CASCADE) 
    role = models.ForeignKey(Role, on_delete= models.CASCADE)

    class Meta:
        managed = True
        db_table = 'user_role'
        unique_together = (('user', 'role'),)


class FilmCategory(models.Model):
    film = models.ForeignKey("Film", on_delete= models.CASCADE)  
    category = models.ForeignKey("Category", on_delete= models.CASCADE)

    class Meta:
        managed = True
        db_table = 'film_category'
        unique_together = (('film', 'category'),)


class FilmCountry(models.Model):
    film = models.ForeignKey("Film", on_delete= models.CASCADE)  
    country = models.ForeignKey("Country", on_delete= models.CASCADE)

    class Meta:
        managed = True
        db_table = 'film_country'
        unique_together = (('film', 'country'),)


class FilmGenre(models.Model):
    film = models.ForeignKey("Film", on_delete= models.CASCADE) 
    genre = models.ForeignKey('Genre', on_delete= models.CASCADE)

    class Meta:
        managed = True
        db_table = 'film_genre'
        unique_together = (('film', 'genre'),)


class FilmPhoto(models.Model):
    film = models.ForeignKey("Film", on_delete= models.CASCADE)
    photo = models.ForeignKey("Photo", models.DO_NOTHING)

    class Meta:

        managed = True
        db_table = 'film_photo'
        unique_together = (('film', 'photo'),)

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

"""Вообще"""
class MemberPost(models.Model):
    member = models.ForeignKey("Member", on_delete= models.CASCADE)
    post = models.ForeignKey('Post', on_delete= models.CASCADE)

    class Meta:
        managed = True
        db_table = 'member_post'
        unique_together = (('member', 'post'),)

"""В фильме"""
class FilmMemberPost(models.Model):
    film = models.ForeignKey(Film, on_delete= models.CASCADE)  
    member = models.ForeignKey('Member',on_delete= models.CASCADE)
    post = models.ForeignKey('Post', on_delete= models.CASCADE)

    class Meta:
        managed = True
        db_table = 'film_member_post'
        unique_together = (('film', 'member', 'post'),)

"""
Избранное
"""
class Favorite(models.Model):
    film = models.ForeignKey('Film', on_delete= models.CASCADE)  
    user = models.ForeignKey("User", on_delete= models.CASCADE)

    class Meta:

        verbose_name = "Любимое"

        managed = True
        db_table = 'favorite'
        unique_together = (('film', 'user'),)

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

"""
Просмотренное
"""
class Viewed(models.Model):
    film = models.ForeignKey("Film", on_delete= models.CASCADE)
    user = models.ForeignKey("User",on_delete= models.CASCADE)

    class Meta:
        verbose_name = "Просмотренное" 
        
        managed = True
        db_table = 'viewed'
        unique_together = (('film', 'user'),)

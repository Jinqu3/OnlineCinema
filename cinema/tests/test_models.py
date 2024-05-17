from django.test import TestCase
from django.urls import resolve,reverse
from cinema.models import Film,Member,Genre,Score,User,ScoreStar,Review

class TestModels(TestCase):

    def setUp(self):
        self.film = Film.objects.create(name='film',url = "film_slug")
        self.user = User.objects.create(name='user',surname ='surname',login='login',password = 'password',email = 'email')
        self.member = Member.objects.create(name='user',surname='surname')

    def test_film_has_already_poster_on_default(self):
        self.assertEqual(self.film.poster,"films/default_film_image.jpg")

    def test_member_has_already_photo_on_default(self):
        self.assertEqual(self.member.photo,"members/default_member_image.jpeg")

    def test_user_has_already_photo_on_default(self):
        self.assertEqual(self.user.photo,"users/default_user_image.jpeg")

    def test_film_average_rating(self):
        self.assertEqual(self.film.get_average_rating(),0)

    def test_user_add_views(self):

        self.user.views.add(self.film)

        self.assertEqual(len(self.user.views.all()),1)
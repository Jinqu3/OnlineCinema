from django.test import TestCase,Client
from django.urls import resolve,reverse
from cinema.models import Film,Member,Genre,Score,User,ScoreStar,Review
from cinema.views import MovieView,FilterMovieView,Search,MovieDetailView,AddStarRating,MemberView,AddToFavoriteView,MarkAsViewedView,AddReviewView

class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.list_url = reverse('list')
        self.detail_url = reverse('film_detail',args=['film_slug'])
        self.film = Film.objects.create(name='film',url = "film_slug")

    def test_film_list_get(self):
        response = self.client.get(self.list_url)

        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,"films/film_list.html")

    def test_film_detail_get(self):
        response = self.client.get(self.detail_url)
        
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,"films/film_detail.html")

    
    # def test_film_detail_POST_add_new_review(self):
    #     user = User.objects.create(
    #         name = "name",
    #         surname = "surname",
    #         login = "user",
    #         email = "email",
    #         password = "password"
    #     )
        
    #     Review.objects.create(
    #         user = user,
    #         film = self.film,
    #         text = "text"
    #     )

    #     response = self.client.post(self.detail_url)

    #     self.assertEqual(response.status_code,302)
    #     self.assertEqual(self.film.reviews.first().film,self.film)
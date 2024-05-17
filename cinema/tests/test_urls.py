from django.test import SimpleTestCase
from django.urls import resolve,reverse

from cinema.views import MovieView,FilterMovieView,Search,MovieDetailView,AddStarRating,MemberView,AddToFavoriteView,MarkAsViewedView,AddReviewView

class TestUrls(SimpleTestCase):

    def test_film_list(self):
        url = reverse('list')
        self.assertEqual(resolve(url).func.view_class,MovieView)

    def test_filter(self):
        url = reverse('filter')
        self.assertEqual(resolve(url).func.view_class,FilterMovieView)

    def test_search(self):
        url = reverse('search')
        self.assertEqual(resolve(url).func.view_class,Search)

    def test_film_detail(self):
        url = reverse('film_detail',args=['some-slug'])
        self.assertEqual(resolve(url).func.view_class,MovieDetailView)

    def test_add_rating(self):
        url = reverse('add-rating',args=['some-slug'])
        self.assertEqual(resolve(url).func.view_class,AddStarRating)

    def test_member_detail(self):
        url = reverse('member_detail',args=['some-slug'])
        self.assertEqual(resolve(url).func.view_class,MemberView)

    def test_add_review(self):
        url = reverse('add_review',args=[0])
        self.assertEqual(resolve(url).func.view_class,AddReviewView)

    def test_add_favorite(self):
        url = reverse('add_to_favorite',args=[0])
        self.assertEqual(resolve(url).func.view_class,AddToFavoriteView)

    def test_add_rating(self):
        url = reverse('mark_as_viewed',args=[0])
        self.assertEqual(resolve(url).func.view_class,MarkAsViewedView)
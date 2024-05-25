"""
URL configuration for OnlineCinema project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from . import views
from django.urls import path

urlpatterns = [
    path("", views.MovieView.as_view(),name="list"),
    path("filter/",views.FilterMovieView.as_view(),name="filter"),
    path("search/",views.Search.as_view(),name="search"),
    path("films/<slug:slug>/",views.MovieDetailView.as_view(),name = "film_detail"),  
    path("<slug:slug>/add-rating/", views.AddStarRating.as_view(), name='add_rating'),
    path("member/<slug:slug>/",views.MemberView.as_view(),name = "member_detail"),  
    path("<int:slug>/",views.AddReviewView.as_view(),name = "add_review"), 
    path('<int:film_id>/favorite/', views.AddToFavoriteView.as_view(), name='add_to_favorite'),
    path('<int:film_id>/viewed/', views.MarkAsViewedView.as_view(), name='mark_as_viewed'),
    path('pdf_film_report/<int:film_id>/', views.generate_film_pdf_report, name='generate_film_pdf_report'),
]
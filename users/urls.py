from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.sign_in, name='login'),
    path('logout/', views.sign_out, name='logout'),
    path('register/', views.sign_up, name='register'),
    path('profile/', views.user_profile, name='user_profile'),
    path('profile/edit/', views.update_profile, name='profile_edit')
]

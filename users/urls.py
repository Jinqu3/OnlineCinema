from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.sign_in, name='login'),
    path('logout/', views.sign_out, name='logout'),
    path('register/', views.sign_up, name='register'),
    path('profile/', views.user_profile, name='profile'),
    path('profile/', views.user_profile, name='user_profile'),
    path('profile/edit/', views.profile_edit, name='profile_edit'),
    path('pdf_report/<int:profile_id>/', views.generate_pdf_report, name='generate_pdf_report'),
]

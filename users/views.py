from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from .forms import LoginForm, RegisterForm,UserProfileForm
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required

from django.http import HttpResponse
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import inch
from reportlab.platypus import Table, TableStyle
from reportlab.lib import colors
from io import BytesIO
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

from cinema.models import User

def sign_in(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('/')

        form = LoginForm()
        return render(request, 'registration/login.html', {'form': form})

    elif request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                messages.success(request, f'Здравствуйте {username.title()}, добро пожаловать!')
                return redirect('/')

        messages.error(request, f'Неверное имя пользователя или пароль')
        return render(request, 'registration/login.html', {'form': form})

def sign_out(request):
    logout(request)
    messages.success(request,f'Вы вышли из системы')
    return redirect('/')

def sign_up(request):
    if request.method == 'GET':
        form = RegisterForm()
        return render(request, 'registration/register.html', {'form': form})

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Вы успешно зарегистрировались')
            return redirect('/')
        else:
            return render(request, 'registration/register.html', {'form': form})



@login_required
def user_profile(request):
    user_profile = get_object_or_404(User, user=request.user)
    return render(request, 'profile/profile.html', {'profile': user_profile}) 

@login_required
def profile_edit(request):
    user_instance = request.user
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=user_instance)
        if form.is_valid():
            form.save()
            return render(request, 'profile/profile_edit.html')
    else:
        form = UserProfileForm(instance=user_instance)
    return render(request, 'profile/profile_edit.html', {'form': form})

def generate_pdf_report(request, profile_id):

    pdfmetrics.registerFont(TTFont('MyFont', 'static/font.ttf'))

    try:
        profile = User.objects.get(id=profile_id)
    except User.DoesNotExist:
        return HttpResponse("User does not exist.")

    buffer = BytesIO()
    pdf = canvas.Canvas(buffer, pagesize=A4)
    pdf.setFont('MyFont', 12)
    pdf.drawString(1*inch, 10*inch, "Отчёт о пользователе: {}".format(profile.surname + " " + profile.name + " " + profile.lastname))
    pdf.drawString(1*inch, 9*inch, "Логин: {}".format(profile.login))
    pdf.drawString(1*inch, 8*inch, "Email: {}".format(profile.email))
    pdf.drawString(1*inch, 7*inch, "Дата рождения: {}".format(profile.date_of_birth))
    pdf.drawString(1*inch, 6*inch, "Пол: {}".format(profile.gender))
    
    favorite_films = profile.get_favorite()
    viewed_films = profile.get_views()
    scores = profile.get_scores()
    
    data = [["Избранное:"]]
    data.extend([[f"Фильм: {film.name}"] for film in favorite_films])
    table = Table(data, colWidths=[6*inch])
    table.setStyle([
        ('FONTNAME', (0,0), (-1,-1), 'MyFont'),
        ('FONTSIZE', (0,0), (-1,-1), 12),
        ('TEXTCOLOR', (0,0), (-1,-1), colors.black),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('ALIGN', (0,0), (-1,-1), 'LEFT'),
    ])
    table.wrapOn(pdf, 6*inch, 4*inch)
    table.drawOn(pdf, 1*inch, 5*inch)
    
    data = [["Просмотренное:"]]
    data.extend([[f"Фильм: {film.name}"] for film in viewed_films])
    table = Table(data, colWidths=[6*inch])
    table.setStyle([
        ('FONTNAME', (0,0), (-1,-1), 'MyFont'),
        ('FONTSIZE', (0,0), (-1,-1), 12),
        ('TEXTCOLOR', (0,0), (-1,-1), colors.black),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('ALIGN', (0,0), (-1,-1), 'LEFT'),
    ])
    table.wrapOn(pdf, 6*inch, 4*inch)
    table.drawOn(pdf, 1*inch, 3*inch)
    
    data = [["Оцененное:"]]
    data.extend([[f"Фильм: {score.film.name}", f"Оценка: {score.star.value}"] for score in scores])
    table = Table(data, colWidths=[3*inch, 3*inch])
    table.setStyle([
        ('FONTNAME', (0,0), (-1,-1), 'MyFont'),
        ('FONTSIZE', (0,0), (-1,-1), 12),
        ('TEXTCOLOR', (0,0), (-1,-1), colors.black),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('ALIGN', (0,0), (-1,-1), 'LEFT'),
    ])
    table.wrapOn(pdf, 6*inch, 4*inch)
    table.drawOn(pdf, 1*inch, 1*inch)
    
    pdf.save()
    buffer.seek(0)
    return HttpResponse(buffer.getvalue(), content_type='application/pdf')
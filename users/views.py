from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from .forms import LoginForm, RegisterForm,UserProfileUpdateForm
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required

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


def update_profile(request):
    if request.method == 'POST':
        user_form = UserProfileUpdateForm(request.POST, request.FILES, instance=request.user)
        if user_form.is_valid():
            user_form.save()
            messages.success(request, 'Ваш профиль успешно обновлен!')
            return redirect('user_profile') 
        else:
            messages.error(request, 'Ошибка при обновлении профиля.')
    else:
        user_profile = get_object_or_404(User, user=request.user)
        user_form = UserProfileUpdateForm(instance=user_profile)
    return render(request, 'profile/profile_edit.html', {'user_form': user_form})
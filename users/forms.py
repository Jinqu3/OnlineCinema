from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.apps import apps
User = apps.get_model('cinema', 'User')

class LoginForm(forms.Form):
    username = forms.CharField(max_length=65)
    password = forms.CharField(max_length=65, widget=forms.PasswordInput)

    class Meta:
        fields = ['username', 'password']

class RegisterForm(UserCreationForm):
    email = forms.CharField(label="Почта")
    name = forms.CharField(label="Имя")
    surname = forms.CharField(label="Фамилия")
    lastname = forms.CharField(label="Отчество")

    class Meta:
        model = get_user_model()
        fields = ['username', 'password1', 'password2', 'email', 'name', 'surname', 'lastname']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.username = user.username.lower()

        if commit:
            user.save()

        user_profile = User.objects.create(
            user=user,
            login=user.username,
            password=user.password,
            name=self.cleaned_data.get("name"),
            surname=self.cleaned_data.get("surname"),
            lastname=self.cleaned_data.get("lastname"),
            email=self.cleaned_data.get("email"),
        )

        return user
    
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'surname', 'lastname', 'date_of_birth', 'gender', 'photo']
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
        }
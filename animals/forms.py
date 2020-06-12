from django import forms
from animals.models import Animals, Usuario


class AnimalsForm(forms.ModelForm):
    class Meta:
        model = Animals
        fields = '__all__'


class LoginForm(forms.Form):
    username = forms.CharField(max_length=128)
    password = forms.CharField(widget=forms.PasswordInput())


class SignUpForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = Usuario
        fields = ['username', 'password', 'email']

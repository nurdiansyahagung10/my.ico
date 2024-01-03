from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User
from django import forms


class UserForm (forms.Form):
    username = forms.CharField(widget=forms.TextInput(
        attrs={"class": "form-control bg-light border-0 shadow-none", "aria-describedby": "emailHelp"}), required=True, max_length=100)
    password = forms.CharField(required=True, widget=forms.PasswordInput(
        attrs={'class': 'form-control bg-light border-0 shadow-none'}))
    rememberme = forms.BooleanField(required=False, widget=forms.CheckboxInput(
        attrs={'class': 'form-check-input', 'id': 'exampleCheck1'}))


class UserChangeForm(UserChangeForm):
    first_name = None
    last_name = None
    class Meta:
        model = User
        fields = ('username', 'email')


class UserCreateForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={"class": "form-control bg-light border-0 shadow-none"}), required=True, max_length=100)
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={"class": "form-control bg-light border-0 shadow-none"}), required=True, max_length=100)
    password1 = forms.CharField(required=True, widget=forms.PasswordInput(
        attrs={'class': 'form-control bg-light border-0 shadow-none'}))
    password2 = forms.CharField(required=True, widget=forms.PasswordInput(
        attrs={'class': 'form-control bg-light border-0 shadow-none'}))
    date_of_birth = forms.DateField(required=True, widget=forms.DateInput(
        attrs={'class': 'form-control bg-light border-0 shadow-none', 'type' : 'date'}))
    pelajar = forms.BooleanField(required=False, widget=forms.CheckboxInput(
        attrs={'class': 'form-check-input', 'id': 'exampleCheck1'}))
    class Meta:
        model = User
        fields = ('username', 'email', 'date_of_birth', 'pelajar',)

class AdminUserCreateForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'date_of_birth', 'pelajar',)

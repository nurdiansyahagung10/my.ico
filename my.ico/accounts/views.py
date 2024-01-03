from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UserForm, UserCreateForm
from django.contrib.auth.hashers import check_password
from django.contrib.auth import authenticate, login, get_user_model
from django.contrib import messages


def SignUpView(request):
    form = UserCreateForm()
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            date_of_birth = form.cleaned_data.get('date_of_birth')
            password = form.cleaned_data.get('password1')
            user =get_user_model().objects.create(username = username, email = email, date_of_birth =date_of_birth, password = password)
            user.save()
            return redirect ('signin')
    return render(request, 'accounts/signup.html', {'form' : form, })        

# Create your views here.
def SignInView(request):
    form = UserForm()
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password') 
            remember_me = form.cleaned_data.get('rememberme')
            auth = authenticate(request, username = username)
            if auth is not None:
                cek_pw = check_password(password, auth.password)
                if cek_pw:
                    if not remember_me:
                        request.session.set_expiry(0)
                    else:
                        request.session.set_expiry(2592000)
                    login(request, auth)
                    return redirect('home')
                else:
                    messages.error(request, 'password is incorret')
            else:
                messages.error(request, 'username or email is incorret')
                return redirect('signin')
    return render (request, 'accounts/signin.html', {'form' : form})
from django.shortcuts import HttpResponse, redirect
from django.contrib.auth import get_user_model

def home(request):
    if(request.user.is_authenticated):
        return HttpResponse(request.user)
    else:
        return redirect('login')
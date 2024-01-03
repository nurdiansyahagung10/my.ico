from django.urls import path
from .views import SignInView,SignUpView
urlpatterns = [
    path("sign-in/", SignInView, name="signin"),
    path("sign-up/", SignUpView, name="signup")
    
]

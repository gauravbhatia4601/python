from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('/accounts/login/', views.login, name='login'),
    path('', login_required(views.home), name='home'),
]

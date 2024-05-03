
from django.urls import path, include
from . import views

urlpatterns = [
    path('create-new-account', views.signup, name='register'),
    path('login', views.login, name='login'),
]

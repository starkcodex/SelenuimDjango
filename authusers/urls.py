
from django.urls import path, include
from . import views

urlpatterns = [
    path('create-new-account', views.signup, name='register'),
    path('user-profile/<str:user_name>', views.profile, name='profile'),
    path('login', views.login, name='login'),
    path('logout', views.logOut, name='logout'),
    path('change_password', views.PasswordChangeView.as_view(template_name= "authors/password_change.html"), name="change-password"),
    path('password_success', views.password_success, name='password_success'),
]

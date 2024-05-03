
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('detail/<str:slug_url>', views.detail, name='detail'),
    path('new-app', views.new_emp, name='new_emp'),
    path('user_profile', views.profile, name='user_profile'),
    path('contact_us', views.contact_us, name='contact_us'),
]

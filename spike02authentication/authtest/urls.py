from django.urls import path
from authtest import views

urlpatterns = [
    path('', views.index),
    path('signup/', views.signup_user),
    path('login/', views.login_user),
    path('logout/', views.logout_user),
]
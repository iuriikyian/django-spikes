from django.urls import path
from testMessages import views

urlpatterns = [
    path('', views.index),
    path('post/', views.post_message),
]
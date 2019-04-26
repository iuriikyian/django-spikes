from django.urls import path
from notes import views

urlpatterns = [
    path('', views.index),
    path('edit/', views.edit),
    path('edit/<int:id>', views.edit),
]
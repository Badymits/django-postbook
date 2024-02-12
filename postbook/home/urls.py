from django.urls import path

from . import views

urlpatterns = [
    path('', views.homePage, name='home'),
    path('create-post/', views.createPost, name='create-post'),
]

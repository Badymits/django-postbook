from django.urls import path

from . import views

urlpatterns = [
    path('', views.homePage, name='home'),
    path('create-post/', views.createPost, name='create-post'),
    path('detail-post/<int:id>/', views.detailPost, name='detail-post'),
    
    path('create-comment/<int:id>/', views.createComment, name='create-comment'),
]

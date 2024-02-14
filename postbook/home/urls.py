from django.urls import path

from . import views

urlpatterns = [
    path('', views.homePage, name='home'),
    path('create-post/', views.createPost, name='create-post'),
    path('detail-post/<int:id>/', views.detailPost, name='detail-post'),
    path('edit-post/<int:id>/', views.editPost, name='edit-post'),
    
    path('create-comment/<int:id>/', views.createComment, name='create-comment'),
    path('edit-comment/<int:id>/', views.editComment, name='edit-comment'),
]

from django.urls import path

from . import views

urlpatterns = [
    path('', views.homePage, name='home'),
    path('create-post/', views.createPost, name='create-post'),
    path('detail-post/<int:id>/', views.detailPost, name='detail-post'),
    path('edit-post/<int:id>/', views.editPost, name='edit-post'),
    path('delete-post/<int:id>/', views.deletePost, name='delete-post'),
    path('like-post/<int:id>/', views.likePost, name='like-post'),
    path('dislike-post/<int:id>/', views.dislikePost, name='dislike-post'),
    
    path('create-comment/<int:id>/', views.createComment, name='create-comment'),
    path('edit-comment/<int:id>/', views.editComment, name='edit-comment'),
    path('delete-comment/<int:id>/', views.deleteComment, name='delete-comment'),
    path('like-comment/<int:id>/', views.likeComment, name='like-comment'),
    path('dislike-comment/<int:id>/', views.dislikeComment, name='dislike-comment'),
]

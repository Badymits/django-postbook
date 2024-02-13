from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.http import HttpResponse, JsonResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core import serializers
import json

from accounts.models import Account
from .models import Post, Comment
from .forms import CreatePostForm, CreateCommentForm

# Create your views here.
def index(request):
    
    return HttpResponse('Hello World!!')

# all funcs will be camel cases
@login_required(login_url='login')
def homePage(request):
    
    posts = Post.objects.all().order_by('-date_posted')
    context = {'user': request.user, 'posts': posts}
    return render(request, 'home/home.html', context)

@login_required(login_url='login')
def createPost(request):
    
    form = CreatePostForm()
    req_user = Account.objects.get(email=request.user.email)
    
    if request.method == 'POST':
        form = CreatePostForm(request.POST, request.FILES)
        
        if form.is_valid():
            post = form.save(commit=False)
            
            post.user = req_user
            form.save()
            
            messages.success(request, 'POST MADE!')
            return redirect('home')
        else:
            print('ERROR')
            messages.error(request, 'Something went wrong...')
            
    context = {'form': form}
    
    return render(request, 'home/create_post.html', context)

@login_required(login_url='login')
def detailPost(request, id):
    
    try:
        post = get_object_or_404(Post, id=id)
 
    except:
        print('ERROR BOSSING')
        messages.error(request, 'Post does not exist')
        return redirect('home')
    context = {'post': post}
    try:
        comments = Comment.objects.filter(main_post=post.id).order_by('-date_posted')
        context['comments'] = comments
    except:
        messages.error(request, 'No Comments')    
        
    
    
    return render(request, 'home/detail_post.html', context)


@login_required(login_url='login')
def editPost(request, id):
    
    pass

@login_required(login_url='login')
def createComment(request, id):
    
    form = CreateCommentForm()
    context = {}
    try:
        main_post = get_object_or_404(Post, id=id)
        print(main_post.id)
    except:
        messages.error(request, 'Post does not exist')
    
    if request.method == 'POST':
        form = CreateCommentForm(request.POST or None, request.FILES or None)
        
        if form.is_valid():
            comment = form.save(commit=False)
            
            comment.main_post = main_post
            comment.user = request.user
            
            # if request.POST['main_comment']:
            #     comment.main_comment = request.POST['main_comment']
            
            comment.save()
            context['message'] = 'Comment Successful'
            messages.success(request, 'Comment Success')
            
            return JsonResponse({
                'comment_user': comment.user.username,
                'comment_body': comment.body,
                'comment_date': comment.date_posted
            })
        else:
            messages.error(request, 'There was an error')
            
    
    
    return JsonResponse(context)
    
    
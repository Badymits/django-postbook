from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.http import HttpResponse, JsonResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core import serializers
import json

from accounts.models import Account
from .models import Post, Comment
from .forms import CreatePostForm, UpdatePostForm, CreateCommentForm, EditCommentForm

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
        print('ERROR')
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
    
    context = {}
    
    try:
        post = get_object_or_404(Post, id=id)
        form = UpdatePostForm(instance=post)
    except:
        messages.error(request, 'Post does not exist')
        return redirect('home')
    
    if request.method == 'POST':
        
        form = UpdatePostForm(request.POST or None, request.FILES or None, instance=post)
        
        if form.is_valid():
            post = form.save(commit=False)
            
            # cleaned data meaning the new data that has been sent thru POST request 
            # and can only be accessed once is_valid has been called
            post.title = form.cleaned_data['title']
            post.body = form.cleaned_data['body']
            
            # check if image has been passed thru
            if form.cleaned_data['image']:
                post.image = form.cleaned_data['image']
            post.save()
            
            messages.success(request, 'Edit Successful!')
            return redirect('detail-post', id)
        else:
            messages.error(request, 'Something went wrong...')
    
    # setting the initial values to be rendered in the form
    form = UpdatePostForm(
        initial={
            'user': post.user,
            'title': post.title,
            'body': post.body,
            'image': post.image
        }
    )
    context['post'] = post
    context['form'] = form
    
    
    return render(request, 'home/edit_post.html', context)


@login_required(login_url='login')
def deletePost(request, id):
    context = {}
    try:
        post = get_object_or_404(Post, id=id)
        post.delete()
        context['message'] = 'Post has been deleted!'
        messages.success(request, 'Post has been deleted')
        return redirect('home')
        
    except:
        context['message'] = 'post not found'
        return JsonResponse(context)


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
            print(request.POST)
            comment = form.save(commit=False)
            
            comment.main_post = main_post
            comment.user = request.user
            
            if request.POST['main_comment'] == False:
                # put in request data the main comment for this line pota
                try:
                    comment.main_comment = comment
                except:
                    print('wtf')
                    messages.error(request, 'cant do that')
            
            comment.save()
            context['message'] = 'Comment Successful'
            messages.success(request, 'Comment Success')
            
            # too lazy but same result (yes, these values can be passed in like the example on line 161). Then pass the context var
            # all together
            return JsonResponse({
                'comment_id': comment.id,
                'comment_user': comment.user.username,
                'comment_body': comment.body,
                'comment_date': comment.date_posted
            })
        else:
            messages.error(request, 'There was an error')
            
    
    
    return JsonResponse(context)

@login_required(login_url='login')
def editComment(request, id):
    
    context = {}
    
    try:
        comment = get_object_or_404(Comment, id=id)
    except:
        context['message'] = 'Comment has been deleted'
        messages.error(request, 'Comment has been deleted')
        
    if request.method == 'POST':
       
        form = EditCommentForm(request.POST or None, instance=comment)
        
        if form.is_valid():
            
            comment = form.save(commit=False)
            comment.body = form.cleaned_data['body']
            
            comment.save()
            
            messages.success(request, 'comment edited')
            context['message'] = 'success'
            context['comment'] = comment.body
            return JsonResponse(context)
        
    context['message'] = 'lods may comment lods'
    context['comment'] = comment.body
    
    return JsonResponse(context)

@login_required(login_url='login')
def deleteComment(request, id):
    
    context = {}
    try:
        comment = get_object_or_404(Comment, id=id)
        
        comment.delete()
        context['message'] = 'Comment Successfully deleted'
        return JsonResponse(context)
    except:
        context['message'] = 'Comment does not exist'
        return JsonResponse(context)
    
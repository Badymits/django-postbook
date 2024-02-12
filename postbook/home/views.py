from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages 
from django.contrib.auth.decorators import login_required

from accounts.models import Account
from .models import Post
from .forms import CreatePostForm

# Create your views here.
def index(request):
    
    return HttpResponse('Hello World!!')

# all funcs will be camel cases
@login_required(login_url='login')
def homePage(request):
    
    posts = Post.objects.all()
    context = {'user': request.user, 'posts': posts}
    return render(request, 'home/home.html', context)

@login_required(login_url='login')
def createPost(request):
    
    form = CreatePostForm()
    req_user = Account.objects.get(email=request.user.email)
    
    if request.method == 'POST':
        form = CreatePostForm(request.POST)
        
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
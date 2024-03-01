from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .models import Account
from home.models import Post, Comment
from .forms import RegisterModelForm, LoginModelForm

# Create your views here.
def loginView(request):
    form = LoginModelForm()
    
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        email=request.POST['email']
        password = request.POST['password']
        try: 
            user = Account.objects.get(email=email)
            print(user.username)
        except:
            messages.error(request, 'User does not exist')
        try:
            # THIS IS VERY MISLEADING POTANGINAAAAAAAAAAAAAAAAAAAAAAAAAA
            # since the username field is set to email, USE THAT INSTEAD TO PASS IN THE USERNAME PARAM
            user = authenticate(username=email, password=password)
        except:
            return redirect('register')
        print(user)
        if user is not None:
            login(request, user)
            print('SUCCESS')
            return redirect('home')
        else:
            print(messages.error)
            messages.error(request, 'Credential Error')
        
    context = {'login_form': form}
    
    return render(request, 'accounts/login.html', context)

def registerView(request):
   
    if request.method == 'POST':
        # add password authentication
        form = RegisterModelForm(request.POST)
        
        if form.is_valid():
            form.save()
            
            messages.success(request, 'Registered Successfully! You may now enter your credentials')
            return redirect('login')
        else:
            messages.error(request, 'Please enter valid information and all')
            
    form = RegisterModelForm()
    context = {'reg_form': form}
    return render(request, 'accounts/register.html', context)

def logoutView(request):
    
    logout(request)
    
    return redirect('login')


@login_required(login_url='login')
def userView(request, id, tab):
    
    context = {}
    
    try:
        user = get_object_or_404(Account, id=id)
        context['user'] = user
        
        if tab == 'posts':
            user_posts = Post.objects.filter(user=user)
            context['user_posts'] = user_posts
            
        elif tab == 'comments':
            user_comments = Comment.objects.filter(user=user).order_by('-date_posted')
            context['user_comments'] = user_comments
        
        return render(request, 'accounts/profile_page.html', context)
    except:
        context['message'] = 'Account does not exist'
        context['posts'] = Post.objects.all()
        return render(request, 'home/home.html',context)
    
    
    
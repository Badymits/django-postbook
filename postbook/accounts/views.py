from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from .models import Account
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
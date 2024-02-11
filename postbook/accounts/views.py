from django.shortcuts import render

from .models import Account
from .forms import RegisterModelForm, LoginModelForm

# Create your views here.
def loginView(request):
    form = LoginModelForm()
    context = {'login_form': form}
    
    return render(request, 'accounts/login.html', context)

def registerView(request):
    form = RegisterModelForm()
    context = {'reg_form': form}
    return render(request, 'accounts/register.html', context)
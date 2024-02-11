from django.shortcuts import render
from django.http import HttpResponse

from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    
    return HttpResponse('Hello World!!')

# all funcs will be camel cases
@login_required(login_url='login')
def homePage(request):
    context = {'user': request.user}
    return render(request, 'home/home.html', context)
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    
    return HttpResponse('Hello World!!')

# all funcs will be camel cases
def homePage(request):

    return render(request, 'home/home.html')
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def index(request):
    print(request.user)
    return render(request, 'authtest/index.html', {
        "user" : request.user
    })

def signup_user(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return HttpResponseRedirect('/') # already authenticated    
        return render(request, 'authtest/signup.html', {})
    if request.method == 'POST':
        data = request.POST
        user = User.objects.create_user(username=data['username'], email=data['email'], password=data['password'] )
        user.save()
        auser = authenticate(request, username=data['username'], password=data['password'])
        #NOTE: admin site allows to login only for stuff
        if auser:
            print('user is authenticated')
        login(request, auser)
        next = request.GET['next']
        if not next:
            next = '/'
        return HttpResponseRedirect(next)

def login_user(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return HttpResponseRedirect('/') # already authenticated    
        return render(request, 'authtest/login.html', {})
    if request.method == 'POST':
        data = request.POST
        auser = authenticate(request, username=data['username'], password=data['password'])
        login(request, auser)
        #NOTE: admin site allows to login only for stuff
        if auser:
            print('user is authenticated')
        next = request.GET['next']
        if not next:
            next = '/'
        return HttpResponseRedirect(next)

def logout_user(request):
    if request.user.is_authenticated:
        logout(request)
    next = request.GET['next']
    if not next:
        next = '/'
    return HttpResponseRedirect(next)


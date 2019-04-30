from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import messages

# Create your views here.

def index(request):
    return render(request, 'testMessages/index.html', {
        "messages" : messages.get_messages(request)
    })

def post_message(request):
    message = request.POST.get('text', None)
    if message:
        messages.add_message(request, messages.INFO, message)
    return HttpResponseRedirect('/')

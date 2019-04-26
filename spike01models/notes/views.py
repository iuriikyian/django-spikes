from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'notes/index.html', {
        "notes" : []
    })

def edit(request):
    return render(request, 'notes/edit.html', {
        "note" : None
    })
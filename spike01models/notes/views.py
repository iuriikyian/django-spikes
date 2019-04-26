from django.shortcuts import render
from django.http import HttpResponseRedirect

from notes.models import Note

# Create your views here.

def index(request):
    return render(request, 'notes/index.html', {
        "notes" : []
    })

def edit(request, id=None):
    if request.method == 'GET':
        n = {}
        if id:
            n = Note.objects.get(pk=id)
        return render(request, 'notes/edit.html', {
            "note" : n
        })
    elif request.method == 'POST':
        print('POST')
        print(request.POST)
        pk = request.POST['pk']
        text = request.POST['text']
        if pk:
            n = Note.objects.get(pk=pk)
            #TODO: error handling
        else:
            n = Note(text=text)
        n.text = text
        n.save()
        return HttpResponseRedirect('/')
            

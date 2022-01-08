from django.shortcuts import render
from .models import NewEntry


# Create your views here.
def journalapphome(request):
    context = {
        'content':'Home page'
    }
    return render(request,'journal/home.html',context)

def journal(request):
    context = {
        'title':'Journal',
        'journal_entries':NewEntry.objects.all()
    }
    return render(request,'journal/entries.html',context)

def journaladdentry(request):
    context = {
        'title':'Add new entry',
        'content':'Add new entry'
    }
    return render(request,'journal/newentry.html',context)
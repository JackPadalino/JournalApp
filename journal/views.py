from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Entry

# Create your views here.
def journalhome(request):
    context = {
        'content':'Home page'
    }
    return render(request,'journal/home.html',context)

@login_required
# in this view we are getting the current authenticated user, then filtering for entries made only by that user
def journal(request):
    user = request.user
    context = {
        'title':'My Journal',
        #'entries':Entry.objects.all(),
        'entries':Entry.objects.filter(author=user)
    }
    return render(request,'journal/journal.html',context)
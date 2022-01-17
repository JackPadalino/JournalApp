#from typing_extensions import Required
from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Entry
from django.views.generic import ListView,DetailView,CreateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
def journalhome(request):
    context = {
        'content':'Home page'
    }
    return render(request,'journal/home.html',context)

'''
@login_required
# in this view we are getting the current authenticated user, then filtering for entries made only by that user
def journal(request):
    user = request.user
    #entries = Entry.objects.all()
    entries = Entry.objects.filter(author=user)
    entries = entries.order_by('-date_posted')
    context = {
        'title':'My Journal',
        'entries':entries
    }
    return render(request,'journal/journal.html',context)
'''

@login_required
def new_entry(request):
    context = {
        'title':'New Entry'
    }
    return render(request,'journal/newentry.html',context)

# here we are going to make a 'class view' that will render a page that allows user to CRUD posts
class EntryListView(ListView):
    def get_queryset(self):
        entries = Entry.objects.filter(author=self.request.user)
        entries = entries.order_by('-date_posted')
        return entries
    template_name = 'journal/journal.html'
    context_object_name = 'entries'

class EntryDetailView(DetailView):
    model = Entry
    template_name ='journal/entry.html'

class EntryCreateView(LoginRequiredMixin,CreateView):
    model = Entry
    fields = ['content']

    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)
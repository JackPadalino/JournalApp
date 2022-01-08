from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm

# Create your views here.
def register(request):
    if request.method=='POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(request,f'Welcome to JournalApp {username}! Your account has been created and you are now able to log in.')
            return redirect('login')
    else:
        form = UserRegisterForm()
        context = {
        'title':'Register',
        'form':form
    }
    return render(request,'users/register.html',context)

@login_required
def profile(request):
    context = {
        'title':'Profile'
    }
    return render(request,'users/profile.html',context)
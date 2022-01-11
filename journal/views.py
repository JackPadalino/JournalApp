from django.shortcuts import render

# Create your views here.
def journalhome(request):
    context = {
        'content':'Home page'
    }
    return render(request,'journal/home.html',context)
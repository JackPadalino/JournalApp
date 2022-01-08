from django.urls import path
from journal import views

urlpatterns = [
    path('', views.journalapphome,name='journalapp-home'),
    path('journal/',views.journal,name='journal'),
    path('addentry/',views.journaladdentry,name='journal-addentry'),
]
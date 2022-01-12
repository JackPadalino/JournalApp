from django.urls import path
from journal import views

urlpatterns = [
    path('', views.journalhome,name='journalhome'),
    path('journal/', views.journal,name='journal'),
]
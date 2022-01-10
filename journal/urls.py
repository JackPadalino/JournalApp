from django.urls import path
from journal import views

urlpatterns = [
    path('', views.journalhome,name='journalhome'),
]
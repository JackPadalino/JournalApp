from django.urls import path
from journal import views
from .views import EntryDetailView, EntryListView

urlpatterns = [
    path('', views.journalhome,name='journalhome'),
    path('journal/', EntryListView.as_view(),name='journal'),
    path('entry/<int:pk>',EntryDetailView.as_view(),name='entry-details'),
    path('newentry/',views.new_entry,name='new-entry'),
    #path('journal/', views.journal,name='journal'),
]
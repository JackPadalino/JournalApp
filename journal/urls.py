from django.urls import path
from journal import views
from .views import EntryDetailView, EntryListView,EntryCreateView

urlpatterns = [
    path('', views.journalhome,name='journalhome'),
    path('journal/', EntryListView.as_view(),name='journal'),
    path('entry/<int:pk>',EntryDetailView.as_view(),name='entry-details'),
    path('entry/new/',EntryCreateView.as_view(),name='new-entry'),
    #path('journal/', views.journal,name='journal'),
]
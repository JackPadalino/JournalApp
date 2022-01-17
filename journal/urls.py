from django.urls import path
from journal import views
from .views import EntryDetailView, EntryListView,EntryCreateView,EntryUpdateView,EntryDeleteView

urlpatterns = [
    path('', views.journalhome,name='journalhome'),
    #path('journal/', views.journal,name='journal'),
    path('journal/', EntryListView.as_view(),name='journal'),
    path('entry/new/',EntryCreateView.as_view(),name='new-entry'),
    path('entry/<int:pk>/',EntryDetailView.as_view(),name='entry-details'),
    path('entry/<int:pk>/update/',EntryUpdateView.as_view(),name='entry-update'),
    path('entry/<int:pk>/delete/',EntryDeleteView.as_view(),name='entry-delete'),
]
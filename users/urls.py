from django.urls import path
from users import views
from django.contrib.auth import views as auth_views
from .views import UserDeleteView

urlpatterns = [
    path('register/', views.register,name='register'),
    path('profile/', views.profile,name='profile'),
    path('login/',auth_views.LoginView.as_view(template_name='users/login.html'),name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='users/logout.html'),name='logout'),
    path('account/<int:pk>/delete/',UserDeleteView.as_view(),name='account-delete'),
]
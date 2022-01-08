from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm, UserCreationForm

# here we are inheriting the user creating form that comes with Django, but we are adding the email field so 
# we can validate a user using their email
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    
    class Meta:
        model = User
        fields = ['username','email','password1','password2']
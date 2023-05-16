from django import forms
from .models import CustomUser, UserRoles
from django.contrib.auth.forms import UserCreationForm
    

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required')
    user_role = forms.ModelChoiceField(queryset=UserRoles.objects.all())

    class Meta:
        model = CustomUser
        fields = ('username', 'password1', 'password2', 'email', 'user_role')
        

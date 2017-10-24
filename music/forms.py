from django.contrib.auth.models import User
from django import forms


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    #widget is to change the password to stars

    class Meta: #information about your class
        model = User
        fields = ['username', 'email', 'password']


from django import forms
from .models import Users

class SignUpForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = ['username', 'password', 'email']
        widgets = {
            'password': forms.PasswordInput()
        }

class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput())

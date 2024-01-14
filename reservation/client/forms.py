from .models import order,Client,ClientTypes,type,name,product,User
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')

class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ('username', 'password')

class orderforms(forms.ModelForm):
    class Meta :
        model=order
        fields="__all__"


class clientforms(forms.ModelForm):
    class Meta :
        model=Client
        fields="__all__"



class clienttypeforms(forms.ModelForm):
    class Meta :
        model=ClientTypes
        fields="__all__"


class productforms(forms.ModelForm):
    class Meta:
        model= product
        fields="__all__"
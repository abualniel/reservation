from .models import order,Client,product,ClientTypes
from django import forms

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
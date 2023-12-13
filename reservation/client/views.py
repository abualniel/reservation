from django.http import HttpResponse
from django.shortcuts import render,redirect
from django import forms
cat=["Food", "Snacks", "Drinks", "Hardware"]
class product(forms.Form) :
 name=forms.CharField()
 category=forms.SelectMultiple(cat)
 description=forms.CharField()
 rating=forms.ChoiceField(widget=forms.RadioSelect)


def index(requset):
 return HttpResponse('ahmad')

def add (requset):
 return render(requset,template_name="add.html")

def addproduct(requset):
 pro=requset.session.get('pro',0)
 pro+=1
 requset.session['pro']=pro

 return render(requset,template_name="product.html",context={'pro':pro})



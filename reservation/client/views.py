from Tools.scripts.make_ctype import method
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django import forms




def validate_login (view_function):
    def wrapper(requset,*arg):
      if requset.method !='GET':
       return redirect(reversed("home"))
      else:
       return view_function(requset,arg)
    return wrapper









def index(requset):
 return HttpResponse('ahmad')

@validate_login
def add (requset):
 return render(requset,template_name="add.html")

def addproduct(requset):
 pro=requset.session.get('pro',0)
 pro+=1
 requset.session['pro']=pro

 return render(requset,template_name="product.html",context={'pro':pro})



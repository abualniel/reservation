from Tools.scripts.make_ctype import method
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django import forms
from .models import order,Client,product,ClientTypes
from .forms import orderforms,clientforms,clienttypeforms,productforms




def validate_login (view_function):
    def wrapper(requset,*arg):
      if requset.method !='GET':
       return redirect(reversed("home"))
      else:
       return view_function(requset,arg)
    return wrapper









def index(requset):
   if requset.method == "POST":
     if "delete" in requset.POST:
        orid=requset.POST['delete']
        order.object.get(pk=orid).delete()
     if "add " in requset.POST:
      orid=requset.POST['add']
      bb1=order.object.get(pk=orid)
      f1=orderforms(instance=bb1)
      return render(requset,template_name="add.html",context={'form':f1})
      order_list=order.object.all()
     return render(requset,template_name="index.html",context={'order':order_list})



def add (requset):
     if requset.method=='POST':
        m1=order.object.get(pk=requset.POST["orid"])
        m2=order(requset.POST["orid"])
        if m2.is_valid():
            m2.save()
     return redirect(reversed("home"))




@validate_login
def add (requset):
    if requset.method=='POST' :
        b2 =orderforms(requset.POST)
        if b2.is_valid() :
             b2.save()
             return  redirect(reversed(""))


def addproduct(requset):
 pro=requset.session.get('pro',0)
 pro+=1
 requset.session['pro']=pro

 return render(requset,template_name="product.html",context={'pro':pro})



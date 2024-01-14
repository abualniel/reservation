
from django.urls import path
from . import views

urlpatterns = {

    path('', views.index, name="index"),
    path('add/',views.add,name="add"),
    path('product/',views.addproduct,name="addproduct"),
    path('register/', views.register, name='register'),
    path('login/', views.user_login(), name='login'),


}

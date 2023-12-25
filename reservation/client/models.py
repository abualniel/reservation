from django.db import models

class product(models.Model) :
 cat = ["Food", "Snacks", "Drinks", "Hardware"]
 pid = models.IntegerField(primary_key=True, max_length=5, default=0)
 name=models.CharField()
 category=models.SelectMultiple(cat)
 description=models.CharField()
 rating=models.ChoiceField(widget=models.RadioSelect)


class order(models.modle):

 order_ID=models.AutoField(max_length=5)
 product_ID=models.AutoField(max_length=5)
 client_ID = models.AutoField(max_length=5)
 order_Date=models.DateField()
 shipping_date=models.DateField()

class ClientTypes(models.Model):

type = models.IntegerField(primary_key=True, max_length=5, default=0)
name = models.CharField(max_length=150, null=False)
description = models.CharField(max_length=500)


def __str__(self):
 return self.name

class Client(models.Model):

gender_choices = [(1, "Male"), (2, "Female")]
cid = models.IntegerField(primary_key=True, max_length=5, default=0)
name = models.CharField(max_length=150, null=False)
gender = models.IntegerField(choices=gender_choices)
email = models.EmailField(unique=True)
birthdate = models.DateField()
type = models.ForeignKey(ClientTypes, on_delete=models.CASCADE, default=0)

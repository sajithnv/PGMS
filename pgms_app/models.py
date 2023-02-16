from django.db import models


class model_register(models.Model):
    uname=models.CharField('User_Name',max_length=100)
    phone_number=models.CharField('Phone_Number',max_length=10,primary_key=True)
    address=models.CharField('Address',max_length=100)
    registered=models.BooleanField(default=False)
    date=models.DateTimeField(auto_now_add=True)
class model_rent(models.Model):
    uname=models.CharField('User_Name',max_length=100)
    phone_number=models.CharField('Phone_Number',max_length=10,null=True)
    amount=models.PositiveIntegerField('Rent',default="6000")
    paid=models.BooleanField(default=True)
    confirm=models.BooleanField(default=False)

from django.shortcuts import render,redirect
from pgms_app.forms import *
from pgms_app.models import *
import datetime

# Create your views here.
def index(request):
    user_in=False
    uname= request.user.username
    register_data = model_register.objects.filter(uname=uname)
    if register_data:
        user_in=True
    return render(request, 'main.html',{'user_in1':user_in})
def contact(request):
    return render(request, 'contact.html')
def profile(request):
    phone1=None
    uname=request.user.username
    registered=model_register.objects.filter(registered=True)
    not_registered=model_register.objects.filter(registered=False)
    not_confirmed=model_rent.objects.filter(confirm=False)
    confirmed=model_rent.objects.filter(confirm=True)

    registered_data=model_register.objects.filter(uname=uname,registered=True)
    rent_paid=model_rent.objects.filter(uname=uname,paid=True)
    phone=model_register.objects.values_list('phone_number').filter(uname=uname)
    for i in phone:
        phone1=i[0]

    form1=form_rent(request.POST or None)
    if form1.is_valid():
    	form1.save()
    	return redirect('pgms1:profile')
    context={
        'registered_data1':registered_data,
        'registered1':registered,
        'not_registered1':not_registered,
        'confirmed1':confirmed,
        'not_confirmed1':not_confirmed,
        'form1':form1,
        'uname1':uname,
        'phone_number1':phone1,
        'rent_paid1':rent_paid,
    }
    return render(request, 'profile.html',context)
def register(request):
    uname=request.user.username
    form1=form_register(request.POST or None)
    if form1.is_valid():
    	form1.save()
    	return redirect('pgms1:index')
    return render(request,'register.html',{'form':form1,'uname':uname})
def register_now(request,pk):
    model_register.objects.filter(phone_number=pk).update(registered=True)
    return redirect('pgms1:profile')
def confirm_now(request,pk):
    model_rent.objects.filter(phone_number=pk).update(confirm=True)
    return redirect('pgms1:profile')
def reset_payment(request):
    model_rent.objects.all().delete()
    return redirect('pgms1:profile')
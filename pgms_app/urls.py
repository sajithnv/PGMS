from django.conf.urls import url
from django.urls import path
from pgms_app.views import *
urlpatterns = [
    url(r'^$',index,name='index'),
    url(r'^profile/$',profile,name='profile'),
    url(r'^contact/$',contact,name='contact'),
    url(r'^register/$',register,name='register'),
    url(r'^register_now/(?P<pk>\d+)$',register_now,name='register_now'),
    url(r'^confirm_now/(?P<pk>\d+)$',confirm_now,name='confirm_now'),
    url(r'^reset_payment/$',reset_payment,name='reset_payment'),

]

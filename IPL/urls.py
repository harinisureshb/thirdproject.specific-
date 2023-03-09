from IPL.views import *
from django.urls import path
app_name='second'
urlpatterns=[
    path('lsg/',lsg,name='lsg'),
    path('csk/',csk,name='csk')
]
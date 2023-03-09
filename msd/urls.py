from msd.views import *
from django.urls import path
app_name='first'
urlpatterns=[
    path('dhoni/',dhoni,name='dhoni'),
    path('virat/',virat,name='virat'),
]
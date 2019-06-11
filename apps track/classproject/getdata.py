

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'classproject.settings')
import django
django.setup()
import click
import openpyxl
from django.db import models

from onlineapp.models import *
def dboperations():
    data = College.objects.all()
    l=len(data)
    print(data)
    for i in range(1,l):
        data=College.objects.get(id=i)
        #print(data.name,end=' ')
        print(data.acronym,end=' ')
        print(data.contact)
        #print(data.location)
    print(l)
    val=College.objects.values()
    print(val)
    data=College.objects.filter(location="hyderabad")
    print(len(data))
    print(College.objects.filter(location="hyderabad").count)
if __name__=='__main__':
    dboperations()








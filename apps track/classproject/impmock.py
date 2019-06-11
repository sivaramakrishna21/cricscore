import requests
from bs4 import BeautifulSoup
import urllib.request
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'classproject.settings')
import django
django.setup()

import click
import openpyxl
from django.db import models

from onlineapp.models import *
@click.group()
def dboperations():
    click.echo("hiii")
    pass


@dboperations.command('importdata',short_help='imports the data from the corresponding excel sheets')
@click.argument('files')
def importhtml(files):
    page=open("marks.html").read()
    s=BeautifulSoup(page,'html.parser')
    t=s.find('table')

    c = 1

    for tr in t.find_all('tr'):
        td=tr.find_all('td')
        row_data=[i.text for i in td]

        if(len(row_data)==7):
           # if (row_data[1] ==None):
                #continue
            print(row_data[1])
            try:

               print(Student.objects.get(id=row_data[0]))
               #print(g)
               c = MockTest1(problem1=row_data[2], problem2=row_data[3], problem3=row_data[4], problem4=row_data[5],
                             total=row_data[6],student=Student.objects.get(id=row_data[0]))
               c.save()
            except Student.DoesNotExist:
                print("hi")
                continue







if __name__=='__main__':
    dboperations()
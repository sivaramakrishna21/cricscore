

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'homeproject.settings')
import django
django.setup()

from django.db import models

from todoapp.models import *

todolist1=['des1',True,"1998-12-10"]
todolist2=['des2',False,'2010-10-10']
todolist3=['des3',True,'2015-10-10']
todolist4=['des4',False,'1999-1-10']
todolist5=['des5',True,'1997-2-2']
todo=['act1','act2','act3','act4','act5']


for i in range(1,6):
    c=Todolist(name=todo[i-1])
    c.save()


c=Todoitem(description=todolist1[0],completed=todolist1[1],duedate=todolist1[2])
c.save()
c=Todoitem(description=todolist2[0],completed=todolist2[1],duedate=todolist2[2])
c.save()
c=Todoitem(description=todolist3[0],completed=todolist3[1],duedate=todolist3[2])
c.save()
c=Todoitem(description=todolist4[0],completed=todolist4[1],duedate=todolist4[2])
c.save()
c=Todoitem(description=todolist5[0],completed=todolist5[1],duedate=todolist5[2])
c.save()
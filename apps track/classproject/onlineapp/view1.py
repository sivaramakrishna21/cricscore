from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context,Template
from onlineapp.models import *
# Create your views here.

def new_page(request):

    str = list(College.objects.values('name', 'acronym'))
    str1 = '<http><body><table border="1">'
    for i in range(0,len(str)):

        str1 += "<tr><td>" + str[i]['name'] + "</td><td>" + str[i]['acronym'] + "</td></tr>"
        i += 1
    str1 += "</table></body></http>"

    return HttpResponse(str1)
def new_page1(request):
    str =College.objects.values('name', 'acronym')
    return render(request,"temp.html",{"query":str})
def getcollegestudents(request,acronym):
    st=MockTest1.objects.values('student__name','total').filter(student__college__acronym=acronym)
    return render(request,"getcollegestudents.html",{"students":st})
#<td><a href="getcollegestudents/{{i.acronym}}">onlineapp/college_student_{{i.acronym}}</a></td>
def coverpage(request):
    str=College.objects.all()
    return render(request,"mainpage.html",{"colleges":str})
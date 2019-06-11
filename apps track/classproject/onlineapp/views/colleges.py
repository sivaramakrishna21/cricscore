from django.views import View
from onlineapp.models import College,MockTest1,Student
from django.http import HttpResponse,HttpResponseRedirect
from  django.shortcuts import render,redirect
from django.urls import resolve
from onlineapp.forms.collegeform import clgfor,studentform,Mocklistform
from django.template import loader
from onlineapp.forms.auth import loginform,signupform
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import Permission

class CollegeView(LoginRequiredMixin,View):
    login_url='/login/'
    def get(self,request,*args,**kwargs):

        if (kwargs):

            colleges=College.objects.get(**kwargs)
            students=list(colleges.student_set.order_by("-mocktest1__total"))
            user_permissions = Permission.objects.filter(user=request.user)
        #colleges=College.objects.all()
            print(user_permissions)

            return render(request,template_name="temp.html",context={"query":colleges,"students":students,'title':'Students from {}|my app'.format(colleges.name),"user_permission":user_permissions})
        else:
            user_permissions = list(Permission.objects.filter(user=request.user).values_list('name'))
            # colleges=College.objects.all()
            user_permissions=[i[0] for i in user_permissions]
            print(user_permissions)
            colleges = College.objects.all()
            return render(request,template_name="collegenames.html",context={"colleges":colleges,"user_permission":user_permissions})

class addcollege(View):
    def get(self,request,*args,**kwargs):
        print("sjdghjs")
        str = resolve(request.path_info).url_name
        if (kwargs and str=="edit list" ):
            print(kwargs)
            college = College.objects.get(**kwargs)
            form = clgfor(instance=college)

            return render(request, 'clgform.html', {'form': form})
        elif(kwargs and str=="delete college"):
            college=College.objects.get(**kwargs)
            college.delete()
            return redirect('/colleges')

        form=clgfor()
        template_name = loader.get_template("clgform.html")
        # context = {'form': form}
        # return HttpResponse(template_name.render(context,request))
        return render(request,template_name='clgform.html',context={'form':form})
    def post(self,request,**kwargs):
        if(kwargs):
            college=College.objects.get(**kwargs)
            form = clgfor(request.POST, instance=college)
            if (form.is_valid()):
                form.save()
            return redirect('/colleges')
        if(kwargs and str.find("delete")):
            college = College.objects.get(**kwargs)
            form = clgfor(request.POST, instance=college)
            if (form.is_valid()):
                form.save()
            return redirect('/colleges')
        else:
            print("hi")
            form=clgfor(request.POST)
            if(form.is_valid()):
                form.save()
            return redirect('/colleges')
# class addstudents(View):
#     def get(self,request,**kwargs):
#         form=studentform()
#         form2=Mocklistform()
#         return render(request,template_name='studentforms.html',context={'form1':form,"form2":form2})
#     def post(self,request,**kwargs):
#         form=studentform(request.POST,)
#         form2=Mocklistform(request.POST)
#         st=form.save(commit=False)


class loginfor(View):
    def get(self,request):
        form=loginform()
        return render(request,template_name='login.html',context={'form':form})
    def post(self,request):
        form=loginform(request.POST)
        user=authenticate(request,username=form.data['username'],password=form.data['password'])
        if user is not None:
            login(request,user)
            return HttpResponseRedirect("/colleges")
        else:
            return HttpResponse("invalid")

class signfor(View):
    def get(self,request):
        form=signupform()
        return render(request,template_name='signup.html',context={'form':form})
    def post(self,request):
        form = signupform(request.POST)
        if(form.is_valid()):
            user=User.objects.create_user(first_name=form.cleaned_data['firstname'],
            last_name=form.cleaned_data['lastname'],username=form.cleaned_data['username'],
                                          password=form.cleaned_data['password'])
            user.save()
        if user is not None:
            login(request,user)
            return HttpResponseRedirect("/colleges")
        return redirect('/login')

class logout_user(View):
    def get(self,request):
        logout(request)
        return HttpResponseRedirect('/login')
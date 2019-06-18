from django.views import View
from cricscore.models import Matches,Deliveries
from django.http import HttpResponse,HttpResponseRedirect
from  django.shortcuts import render,redirect
from django.template import loader
from django.contrib import messages
from django.db.models import *
from cricscore.forms.auth import loginform,signupform
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import Permission


class matchView(View):
    def get(self,request,season=None,id=None,id1=8):

        if (season):
            if not request.user.is_authenticated:
                return redirect('/login/')
            print(request.user)
            matches=Matches.objects.filter(season=season)
            if(id):

                matches = Matches.objects.get(season=season,id=id)
                print(id,season)
                print(matches)

                delivery=Deliveries.objects.filter(match_id=id)
                # bowlteam=delivery[0]['bowling_team']
                # bowlteam=delivery[0]['bowling_team']
                # totalscore=Deliveries.objects.filter(match_id=id).values('batting_team').annotate(total=Sum('total_runs'))
                # pr
                d = Deliveries.objects.filter(match_id=id).values('batsman').annotate(total=Sum('total_runs')).order_by(
                    '-total')[:3]
                top3wicketgetters=Deliveries.objects.exclude(player_dismissed='null').filter(match_id=id).values('bowler').annotate(total=Count('player_dismissed')).order_by('-total')[:3]
                return render(request,template_name="matchsummary.html",context={"matches":matches,"season":season,"delivery":delivery,"top3":d,"top3wick":top3wicketgetters,"user":request.user})
            if(id1):
                print("hi")
                if(season!=2017 and id1<60):
                    print("hrllo")
                    mat=Matches.objects.filter(season=season).values('id')

                    print(mat[0]['id'])
                    id1+=mat[0]['id']
                print(id1)
                while(1):
                    matches = Matches.objects.filter(season=season,id__range=(id1-7,id1))
                    if(len(matches)==0):
                        id1+=8
                    else:
                        break

                print(matches)
            return render(request,template_name="seasonmatches.html",context={"matches":matches,"season":season,"some":id1,"user":request.user})
        else:

            matches=Matches.objects.filter(season=2019)
            return render(request,template_name="totalmatches.html",context={"matches":matches,"season":2019,"some":8})



class loginfor(View):
    def get(self,request):
        form=loginform()
        return render(request,template_name='login.html',context={'form':form})
    def post(self,request):
        form=loginform(request.POST)
        user=authenticate(request,username=form.data['username'],password=form.data['password'])
        if user is not None:
            login(request,user)
            return HttpResponseRedirect("/home")
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

class displaypoints(View):
    def get(self,request,season):
        if(season):
            d = Matches.objects.filter(season=season).values('winners').annotate(total=2 * Count('winners')).order_by(
                '-total')
            d1= Matches.objects.filter(season=season, winners__isnull=True).values('team1', 'team2')
            print(d)
            for i in d:
                count=0
                if len(d1)==0:
                    break
                for j in d1:
                    if i['winners']==j['team1'] or i['winners']==j['team2']:
                        count+=1
                i['total']+=count

            return render(request,template_name="pointstable.html",context={"points":d,"season":season})

class displayteamdetails(View):
    def get(self,request,team):
        dict=[]
        teamstatus = []
        for i in range(2008,2020):
            f=0
            some=[]
            some.append(i)
            d=list(Matches.objects.filter(team1=team,season=i))
            d1=list(Matches.objects.filter(team2=team,season=i))
            d2=d+d1
            d3 = Matches.objects.filter(season=i).values('winners').annotate(total=2 * Count('winners')).order_by(
                '-total')
            d4 = Matches.objects.filter(season=i, winners__isnull=True).values('team1', 'team2')
            for k in d3:
                count=0
                if len(d4)==0:
                    break
                for j in d4:
                    if k['winners']==j['team1'] or k['winners']==j['team2']:
                        count+=1
                k['total']+=count
            win=Matches.objects.filter(season=i).values('winners','team1','team2')
            winn=win[len(win) - 1]['winners']

            for t in d3:
                if(t['winners']==team):
                    some.append(t['total'])
            d3=d3[:4]
            if(winn==team):
                some.append("champion")
                f=1
            elif(win[len(win) - 1]['team1']!=winn and win[len(win) - 1]['team1']==team):
                some.append("runner")
                f=1
            elif(win[len(win) - 1]['team2']!=winn and win[len(win) - 1]['team2']==team):
                some.append("runner")
                f=1
            else:
                for t in d3:
                    if(team==t['winners']):
                        some.append("playoffs")
                        f=1
                        break
            if(f==0):
                some.append("leaguestage")

            print(some)
            teamstatus.append(some)
            dict.append(d2)


        print(dict)
        return render(request,template_name="teamdetails.html",context={"all":dict,'req':2008,"status":teamstatus})

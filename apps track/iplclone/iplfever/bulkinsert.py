import openpyxl
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'iplfever.settings')
import django
django.setup()
from cricscore.models import *

def bulkinsert():
    wb = openpyxl.load_workbook('C:\\Users\\Siva Rama Krishna\\iplfever\\deliveries.xlsx')
    # db = MySQLdb.connect(host='localhost', user='root', passwd='Root@123')
    # cur = db.cursor()
    # cur.execute('use iplclonedb')
    ws = wb.active
    flag = 0
    row = 1
    li=[]
    for i in ws:
        if flag==0:
            flag=1
            continue
        if row<160000:
            row+=1
            continue
        i1=[]
        for j in i:
            try:
                val = int(j.value)
                i1.append(val)
            except:
                if j.value == None:
                    st = ''
                else:
                    st = j.value
                i1.append(st)
        li.append(Deliveries(match_id_id=i1[0],inning=i1[1],batting_team=i1[2],bowling_team=i1[3],over=i1[4],
                   ball=i1[5],batsman=i1[6],non_striker=i1[7],
                   bowler=i1[8],is_super_over=i1[9],wide_runs=i1[10],bye_runs=i1[11],legbye_runs=i1[12]
                   ,noball_runs=i1[13],penalty_runs=i1[14],batsman_runs=i1[15],
                    extra_runs=i1[16],total_runs=i1[17],player_dismissed=i1[18],dissmisal_kind=i1[19],fielder=i1[20]))
        row+=1
        if row==180000:
            break
    Deliveries.objects.bulk_create(li)

if __name__=='__main__':
    bulkinsert()
#import datetime
import json
import os

import openpyxl
from django.db import connection,DatabaseError
from django.db.models import Max
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, redirect
from .models import *
from datetime import datetime
#import datetime
from ultimatix import config
# Create your views here.
def dictfetchall(cursor):
    """Return all rows from a cursor as a dict"""
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]

def home_view(request):
    try:
        logged_in = request.session['eid']
    except:
        logged_in = False

    if logged_in:
        user = Employee.objects.get(e_id=logged_in)
        return render(request, 'ultimatix/admin/adminhome.html',{'user':user})
    else:
        request.session['eid'] = None
        return redirect('ultimatix:show_login')




def designation_view(request):
    if request.is_ajax() and request.GET:
        try:
            cd = request.GET.get('cd')
            #print("code : "+cd)
            cursor = connection.cursor()
            sql = """
            select d_cd,d_desc,d_min,d_max,d_role from ultimatix_designation 
        	where d_cd=%s
            """
            cursor.execute(sql,[cd])
            #print("cursor : "+str(cursor))
            dict = dictfetchall(cursor)
            #print(str(dict))
            r = json.dumps(dict[0])
            cursor.close()
            return JsonResponse(r, safe=False)
        except DatabaseError  as e:
            print('Database error : ' + str(e))
        finally:
            if cursor:
                cursor.close()


    elif request.method=='POST':
        # return HttpResponse('submitted')
        cd = request.POST.get("cd")
        desc = request.POST.get("desc")

        if (request.POST.get("minexp").strip()) == '':
            min_exp = None
        else:
            min_exp = int(request.POST.get("minexp"))

        if (request.POST.get("maxexp").strip()) == '':
            max_exp = ''
        else:
            max_exp = int(request.POST.get("maxexp"))

        r_type = request.POST.get("role_select")
        # print('r_type : '+'*'+str(r_type)+'*')
        r_num = -1
        if r_type == "Employee":
            r_num = 1
        elif r_type == "HR":
            r_num = 2
        if request.POST.get("add"):
            ob=Designation.objects.filter(d_cd=cd)
            if ob:
                logged_in = request.session['eid']
                user = Employee.objects.get(e_id=logged_in)
                obj = Designation.objects.all().exclude(d_role=0)
                return render(request, 'ultimatix/admin/designation.html',
                             {'error': ' Designation already exists !','obj':obj,'user':user})
            else:
                try:
                    print('Entered for new save')
                    cursor = connection.cursor()
                    sql="""
                    insert into ultimatix_designation(d_cd,d_desc,d_min,d_max,d_role)
                    values(%s,%s,%s,%s,%s)
                    """
                    cursor.execute(sql, (cd, desc, min_exp, max_exp, r_num))
                    connection.commit()
                    cursor.close()
                    #obj=Designation.objects.create(d_cd=cd,d_desc=desc,d_min=min_exp,d_max=max_exp,d_role=r_num)
                    #obj.save()
                    logged_in = request.session['eid']
                    user = Employee.objects.get(e_id=logged_in)
                    obj = Designation.objects.all().exclude(d_role=0)
                    return render(request, 'ultimatix/admin/designation.html',
                              {'success': ' Data saved successfully!','obj':obj,'user':user})
                except DatabaseError  as e:
                    print('Database error : '+str(e))
                    connection.rollback()
                    obj = Designation.objects.all().exclude(d_role=0)
                    logged_in = request.session['eid']
                    user = Employee.objects.get(e_id=logged_in)
                    return render(request, 'ultimatix/admin/designation.html',
                              {'error': ' Database error.Please contact system admin!','obj':obj,'user':user})
                finally:
                    if cursor:
                        cursor.close()
        elif request.POST.get("update"):
            ob = Designation.objects.filter(d_cd=cd)
            if ob:
                logged_in = request.session['eid']
                user = Employee.objects.get(e_id=logged_in)
                Designation.objects.filter(d_cd=cd).update(d_desc=desc,d_min=min_exp,d_max=max_exp,d_role=r_num)
                obj = Designation.objects.all().exclude(d_role=0)
                return render(request, 'ultimatix/admin/designation.html',
                             {'success': ' Data saved successfully!','obj':obj,'user':user})
            else:
                logged_in = request.session['eid']
                user = Employee.objects.get(e_id=logged_in)
                obj = Designation.objects.all().exclude(d_role=0)
                return render(request, 'ultimatix/admin/designation.html',
                             {'error': ' Designation does not exist !','obj':obj,'user':user})
    else:
        logged_in = request.session['eid']
        user = Employee.objects.get(e_id=logged_in)
        obj=Designation.objects.all().exclude(d_role=0)
        return render(request,'ultimatix/admin/designation.html',{'obj':obj,'user':user})



def roles_view(request):
    if request.is_ajax() and request.GET:
        cd=request.GET.get('cd')
        try:
            cursor = connection.cursor()
            sql="""
            select r_cd,r_desc,r_active from ultimatix_project_roles
            where r_cd=%s
            """
            cursor.execute(sql, [cd])
            dict = dictfetchall(cursor)
            r = json.dumps(dict[0])
            cursor.close()
            return JsonResponse(r, safe=False)
        except DatabaseError  as e:
            print('Database error : ' + str(e))
        finally:
            if cursor:
                cursor.close()

    elif request.method=='POST':
        cd=request.POST.get("role_cd")
        desc=request.POST.get("role_desc")
        active=str(request.POST.get("chk_act"))
        updt=str(datetime.now())
        if active !='Y':
            active='N'
        if request.POST.get("add"):
            p_obj=Project_roles.objects.filter(r_cd=cd)
            if p_obj:
                obj = Project_roles.objects.all()
                logged_in = request.session['eid']
                user = Employee.objects.get(e_id=logged_in)
                return render(request, 'ultimatix/admin/roles.html',
                              {'error': ' Project role already exists !', 'obj': obj,'user':user})
            else:
                ob=Project_roles.objects.create(r_cd=cd,r_desc=desc,r_active=active,r_updt=updt)
                ob.save()

                obj = Project_roles.objects.all()
                logged_in = request.session['eid']
                user = Employee.objects.get(e_id=logged_in)
                return render(request, 'ultimatix/admin/roles.html', {'success': ' Data saved successfully!','obj': obj,'user':user})
        elif request.POST.get("update"):
            ob = Project_roles.objects.filter(r_cd=cd)
            if ob:
                logged_in = request.session['eid']
                user = Employee.objects.get(e_id=logged_in)
                Project_roles.objects.filter(r_cd=cd).update(r_desc=desc,r_active=active,r_updt=updt)
                obj = Project_roles.objects.all()
                return render(request, 'ultimatix/admin/roles.html',
                             {'success': ' Data saved successfully!','obj':obj,'user':user})
            else:
                logged_in = request.session['eid']
                user = Employee.objects.get(e_id=logged_in)
                obj = Project_roles.objects.all()
                return render(request, 'ultimatix/admin/roles.html',
                             {'error': ' Role does not exist !','obj':obj,'user':user})

    else:
        logged_in = request.session['eid']
        user = Employee.objects.get(e_id=logged_in)
        obj = Project_roles.objects.all()
        return render(request,'ultimatix/admin/roles.html',{'obj':obj,'user':user})


def regemp_view(request):
    if request.method == 'POST':
        if(request.POST.get('register')):
            #return HttpResponse('Hi')
            fname=request.POST.get('fname')
            lname=request.POST.get('lname')
            sname=request.POST.get('surname')
            dob=request.POST.get('dob')
            bgroup=request.POST.get('bgroup')
            mstatus=request.POST.get('mstatus')
            nationality=request.POST.get('nationality')
            disb=request.POST.get('chk_disb')
            if not disb:
                disb='N'

            gender=request.POST.get('gender')

            paddr1=request.POST.get('paddr1')
            paddr2=request.POST.get('paddr2')
            paddr3=request.POST.get('paddr3')
            caddr1=request.POST.get('caddr1')
            caddr2=request.POST.get('caddr2')
            caddr3=request.POST.get('caddr3')
            email=request.POST.get('email')
            mnumber=request.POST.get('mnumber')

            doj=request.POST.get('doj')
            qfn=request.POST.get('qfn')
            prev_exp=str(request.POST.get('prev_exp'))
            if not prev_exp:
                prev_exp=0
            prev_cmp=request.POST.get('prev_cmp')


            idob = id_select.objects.get(id_desc='e_id')
            id = idob.id_val

            status='Y'
            pwd=str(id)+'@'+dob
            des=request.POST.get('desig_select')
            sal=request.POST.get('salary')
            des_id=Designation.objects.get(d_cd=des).d_id
            des_sdate=str(datetime.today().strftime('%Y-%m-%d'))
            #return HttpResponse(des_sdate)
            eobj=Employee.objects.create(e_id=id,e_fname=fname,e_lname=lname,e_sname=sname,e_dob=dob,e_bgroup=bgroup,
                                         e_mstatus=mstatus,e_nationality=nationality,e_disb=disb,e_gender=gender,
                                         e_paddr1=paddr1,e_paddr2=paddr2,e_paddr3=paddr3,e_caddr1=caddr1,
                                         e_caddr2=caddr2,e_caddr3=caddr3,e_email=email,e_mnumber=mnumber,e_doj=doj,
                                         e_qfn=qfn,e_prev_exp=prev_exp,e_prev_cmp=prev_cmp,e_cl='2',e_sl='2',e_el='4',
                                         e_fl='2',e_status=status,e_pwd=pwd)
            eobj.save()
            e=Employee.objects.get(e_id=id)
            #return HttpResponse(e.e_id)
            #desobj=Employee_desig.objects.create(ed_eid=id,ed_did=e,ed_sdate=des_sdate,ed_status='Y')
            desobj = Employee_desig.objects.create(ed_eid=Employee.objects.get(e_id=id),
                                                   ed_did=Designation.objects.get(d_id=des_id), ed_sdate=des_sdate,
                                                   ed_status='Y')
            desobj.save()
            salob = Employee_sal.objects.create(es_eid=Employee.objects.get(e_id=id), es_ctc=sal, es_sdate=des_sdate,
                                                es_status='Y')
            salob.save()


            idob.id_val = id + 1
            idob.save()
            logged_in = request.session['eid']
            user = Employee.objects.get(e_id=logged_in)
            dobj = Designation.objects.all().exclude(d_role=0)
            return render(request,'ultimatix/admin/addemp.html',{'success':' Data saved successfully !','dobj':dobj,'user':user})
    else:
        try:
            logged_in = request.session['eid']
        except:
            logged_in = False
        if logged_in:
            user=Employee.objects.get(e_id=logged_in)
            dobj=Designation.objects.all().exclude(d_role=0)
            return render(request,'ultimatix/admin/addemp.html',{'dobj':dobj,'user':user})
        else:
            request.session['eid'] = None
            return redirect('ultimatix:show_login')

def viewemp_view(request):

    #eobj=Employee.objects.all().exclude(e_id='1022890')
    cursor = connection.cursor()
    sql = '''
    select ue.e_id, (ue.e_fname ||' ' ||ue.e_lname) as Name, ue.e_gender, ue.e_doj, ud.d_desc, ues.es_ctc, ue.e_status
    from ultimatix_employee ue
    left outer join ultimatix_employee_desig ued on ued.ed_eid_id = ue.e_id
    left outer join ultimatix_designation ud on ud.d_id = ued.ed_did_id
    left outer join ultimatix_employee_sal ues on ues.es_eid_id = ue.e_id
    where ued.ed_status = 'Y' and ud.d_cd!='SYSADMIN' and ues.es_status = 'Y'
    '''
    cursor.execute(sql)
    res = cursor.fetchall()
    res_list = []
    for r in res:
        t = {}
        t['eid'] = r[0]
        t['name'] = r[1]
        t['gender']=r[2]
        t['doj']=r[3]
        t['desig']=r[4]
        t['ctc']=r[5]
        t['status']=r[6]
        res_list.append(t)
    cursor.close()
    logged_in = request.session['eid']
    user = Employee.objects.get(e_id=logged_in)
    return render(request,'ultimatix/admin/viewemp.html',{'eobj':res_list,'user':user})


def updtemp_view(request,pk=0):
    if pk!=0:
        eobj=Employee.objects.get(e_id=pk)
        #d1=str(eobj.e_dob)
        dobj = Designation.objects.all().exclude(d_role=0)
        empdesobj=Employee_desig.objects.get(ed_eid=pk,ed_status='Y').ed_did
        empsalobj=Employee_sal.objects.get(es_eid=pk,es_status='Y')
        return render(request, 'ultimatix/admin/updt_emp.html', {'eobj': eobj,
                                                                 'dobj':dobj,
                                                                 'empdesobj':empdesobj,
                                                                 'empsalobj':empsalobj})
        #return HttpResponse(pk)
    elif pk==0:
        eid=request.POST.get('eid')
        lname = request.POST.get('lname')
        sname = request.POST.get('surname')
        bgroup = request.POST.get('bgroup')
        mstatus = request.POST.get('mstatus')
        disb = request.POST.get('chk_disb')
        if not disb:
            disb = 'N'
        paddr1 = request.POST.get('paddr1')
        paddr2 = request.POST.get('paddr2')
        paddr3 = request.POST.get('paddr3')
        caddr1 = request.POST.get('caddr1')
        caddr2 = request.POST.get('caddr2')
        caddr3 = request.POST.get('caddr3')
        email = request.POST.get('email')
        mnumber = request.POST.get('mnumber')
        qfn = request.POST.get('qfn')
        des = request.POST.get('desig_select')
        des_id = Designation.objects.get(d_cd=des).d_id
        print(des_id)
        ob = Employee_desig.objects.filter(ed_eid=eid, ed_did=des_id, ed_status='Y')
        if not ob:
            des_sdate = str(datetime.today().strftime('%Y-%m-%d'))
            des_edate = str(datetime.today().strftime('%Y-%m-%d'))
            Employee_desig.objects.filter(ed_eid=eid,ed_status='Y').update(ed_edate=des_edate,ed_status='N')
            desobj = Employee_desig.objects.create(ed_eid=Employee.objects.get(e_id=eid),
                                                   ed_did=Designation.objects.get(d_id=des_id), ed_sdate=des_sdate,
                                                   ed_status='Y')
            desobj.save()
        sal = request.POST.get('salary')
        if(float(sal)!=(Employee_sal.objects.get(es_eid=eid,es_status='Y').es_ctc)):
            sal_sdate = str(datetime.today().strftime('%Y-%m-%d'))
            sal_edate = str(datetime.today().strftime('%Y-%m-%d'))
            Employee_sal.objects.filter(es_eid=eid,es_status='Y').update(es_edate=sal_edate,es_status='N')
            salob = Employee_sal.objects.create(es_eid=Employee.objects.get(e_id=eid), es_ctc=sal, es_sdate=sal_sdate,
                                                es_status='Y')
            salob.save()
            #return HttpResponse('salary updated successfully')
            #return HttpResponse(str(eid)+lname+sname)


        Employee.objects.filter(e_id=eid).update(e_lname=lname,e_sname=sname,e_bgroup=bgroup,
                                                 e_mstatus=mstatus,e_disb=disb,e_paddr1=paddr1,
                                                 e_paddr2=paddr2,e_paddr3=paddr3,e_caddr1=caddr1,
                                                 e_caddr2=caddr2,e_caddr3=caddr3,e_email=email,
                                                 e_mnumber=mnumber,e_qfn=qfn)


        return redirect('ultimatix:view_emp')


def crtprj_view(request):
    if request.method=='POST':
        if request.POST.get('create'):
            title=request.POST.get('tle')
            desc=request.POST.get('desc')
            sdate=request.POST.get('sdate')
            expedate=request.POST.get('expedate')
            #crtd=request.POST.get('crtd')
            #eid=config.eid
            #efname = config.efname
            client=request.POST.get('client')
            cloc=request.POST.get('loct')
            complexity=request.POST.get('size_select')
            type=request.POST.get('type_select')
            budget=request.POST.get('budget')
            if budget:
                budget=float(request.POST.get('budget'))
            else:
                budget=0.0
            logged_in = request.session['eid']
            crtd=Employee.objects.get(e_id=logged_in).e_fname
            if expedate:
                obj=Project.objects.create(ptitle=title,pdesc=desc,psdate=sdate,pexpedate=expedate,pcrtd=crtd,pclient=client,powner=Employee.objects.get(e_id=logged_in),pstatus='A',pcloc=cloc,pcomplexity=complexity,ptype=type,pbudget=budget)
                obj.save()
                id_max = Project.objects.all().aggregate(Max('pid'))['pid__max']
                ob1=Project_members.objects.create(pid=Project.objects.get(pid=id_max),
                                            eid=Employee.objects.get(e_id=logged_in),
                                            rid=Project_roles.objects.get(r_cd='OWN'),
                                            pmsdate=sdate,pmstatus='Y')
                ob1.save()
            else:
                obj = Project.objects.create(ptitle=title, pdesc=desc, psdate=sdate, pcrtd=crtd,pclient=client, powner=Employee.objects.get(e_id=logged_in), pstatus='A',pcloc=cloc,pcomplexity=complexity,ptype=type,pbudget=budget)
                obj.save()
                id_max = Project.objects.all().aggregate(Max('pid'))['pid__max']
                ob1=Project_members.objects.create(pid=Project.objects.get(pid=id_max),
                                            eid=Employee.objects.get(e_id=logged_in),
                                            rid=Project_roles.objects.get(r_cd='OWN'),
                                            pmsdate=sdate,pmstatus='Y')
                ob1.save()

            user = Employee.objects.get(e_id=logged_in)
            return render(request, 'ultimatix/admin/create_project.html', {'user':user,'success':'Data saved successfully'})

            #return HttpResponse('submitted : '+cloc+complexity+type+str(budget))

    else:
        try:
            logged_in = request.session['eid']
        except:
            logged_in = False
        if logged_in:
            user=Employee.objects.get(e_id=logged_in)

            return render(request, 'ultimatix/admin/create_project.html', {'user':user})
        else:
            request.session['eid'] = None
            return redirect('ultimatix:show_login')

def show_login(request):
    if request.method=='POST':
        if request.POST.get('login'):
            eid=request.POST.get('eid')
            pwd=request.POST.get('pwd')
            obj=Employee.objects.filter(e_id=eid,e_pwd=pwd).first()
            if not obj:
                config.eid = ""
                config.efname =""
                request.session['eid'] = None
                return render(request, 'ultimatix/login.html',{'error':'Incorrect Employee Id or Password'})
            else:
                request.session['eid'] = eid
                config.eid = Employee.objects.filter(e_id=eid, e_pwd=pwd).first().e_id
                config.efname=Employee.objects.filter(e_id=eid, e_pwd=pwd).first().e_fname
                return redirect('ultimatix:home_view')

    else:
        config.eid=""
        config.efname =""
        request.session['eid'] = None
        return render(request,'ultimatix/login.html')


def proejcts_view(request):
    try:
        logged_in = request.session['eid']
    except:
        logged_in = False
    if logged_in:
        user = Employee.objects.get(e_id=logged_in)
        pobj=Project.objects.all()
        return render(request,'ultimatix/admin/viewprojects.html',{'pobj':pobj,'user':user})
    else:
        request.session['eid'] = None
        return redirect('ultimatix:show_login')

def updtproj_view(request,pid):
    if pid!=0:
        if request.method=='POST':
            if request.POST.get('update'):
                desc=request.POST.get('desc')
                expedate=request.POST.get('expedate')
                client=request.POST.get('client')
                status = request.POST.get('status')
                if expedate:
                    if status=='C':
                        edate = str(datetime.today().strftime('%Y-%m-%d'))
                        Project.objects.filter(pid=pid).update(pdesc=desc, pexpedate=expedate, pedate=edate,pclient=client,
                                                               pstatus=status)
                        return redirect('ultimatix:view_project')
                    elif status=='A':
                        Project.objects.filter(pid=pid).update(pdesc=desc,pexpedate=expedate,pclient=client,pstatus=status)
                        return redirect('ultimatix:view_project')

                else:
                    if status=='C':
                        edate = str(datetime.today().strftime('%Y-%m-%d'))
                        Project.objects.filter(pid=pid).update(pdesc=desc, pedate=edate,pclient=client,
                                                               pstatus=status)
                        return redirect('ultimatix:view_project')
                    elif status=='A':
                        Project.objects.filter(pid=pid).update(pdesc=desc,pclient=client,pstatus=status)
                        return redirect('ultimatix:view_project')
                    #Project.objects.filter(pid=pid).update(pdesc=desc, pclient=client,pstatus=status)
                    #return redirect('ultimatix:view_project')
        else:

            pobj=Project.objects.get(pid=pid)
            return render(request,'ultimatix/admin/updt_project.html',{'pobj':pobj})
    elif pid==0:
        return HttpResponse(pid)


def allocate_view(request):
    if request.is_ajax() and request.GET:
        desid = request.GET.get('desid')
        cursor = connection.cursor()
        if int(desid)!=0:
            #print('desid not 0')
            sql = """
            select e_id,(e_fname||" "||ifnull(e_lname,"")) from ultimatix_employee where e_id in(select es.ed_eid_id from 
            ultimatix_employee_desig es where es.ed_did_id=%s and es.ed_status='Y') and 
            e_status='Y' order by e_id
            """
            cursor.execute(sql,[desid])
        else:
            sql = """
            select e_id,(e_fname||" "||ifnull(e_lname,"")) from ultimatix_employee where e_id in(select es.ed_eid_id from 
            ultimatix_employee_desig es where es.ed_did_id!='16' and es.ed_status='Y') and 
            e_status='Y' order by e_id
            """
            cursor.execute(sql)
        res=cursor.fetchall()
        res_list=[]
        for r in res:
            t={}
            t['eid']=r[0]
            t['ename']=r[1]
            res_list.append(t)
        j=json.dumps(res_list)
        cursor.close()
        #print('called')
        #print('result : '+str(res_list))
        return JsonResponse(res_list, safe=False)
    elif request.method=='POST':
        pid=request.POST.get('pid')
        eid = request.POST.get('eid')
        #print('Employee id: '+eid)
        rid=request.POST.get('role_select')
        desig_cd=Designation.objects.get(d_id=int(request.POST.get('desig_select'))).d_cd
        sdate=str(datetime.now())

        #### if employee is assigned to same project already
        cursor = connection.cursor()
        sql = """
        select eid_id from ultimatix_project_members where eid_id=%s 
        and pmstatus='Y'
        """
        cursor.execute(sql,[eid])
        res=cursor.fetchall()
        #print('result : '+str(res))

        #### if project have an active hr
        sql='''
        select ue.e_id
        from ultimatix_employee ue
        left outer join ultimatix_project_members upm on upm.eid_id = ue.e_id
        left outer join ultimatix_project_roles up on up.r_id = upm.rid_id
        where upm.pmstatus = 'Y' and up.r_cd='MNG' and ue.e_status = 'Y' and upm.pid_id=%s
        '''
        cursor.execute(sql, [pid])
        res1=cursor.fetchall()

        sql='''
        select ue.e_id
        from ultimatix_employee ue
        left outer join ultimatix_project_members upm on upm.eid_id = ue.e_id
        left outer join ultimatix_project_roles up on up.r_id = upm.rid_id
        where upm.pmstatus = 'Y' and up.r_cd='PM' and ue.e_status = 'Y' and upm.pid_id=%s        
        '''
        cursor.execute(sql, [pid])
        res2=cursor.fetchall()


        cursor.close()
        if res:
            #if employee is assigned to same project already
            print('case 1')
            logged_in = request.session['eid']
            user = Employee.objects.get(e_id=logged_in)
            result=default_allocate_view()
            return render(request,'ultimatix/admin/allocate.html',{'pobj': result[0], 'dobj': result[1], 'eobj': result[2], 'robj': result[3],'error':' Employee is already allocated !','user':user})
        elif not res1 and (desig_cd not in ('HR','HR-M')):
            #if project does not have an HR nad currently not assigning an HR
            print('case 2')
            logged_in = request.session['eid']
            user = Employee.objects.get(e_id=logged_in)
            #print('role id : '+str(rid))
            result = default_allocate_view()
            return render(request, 'ultimatix/admin/allocate.html',
                          {'pobj': result[0], 'dobj': result[1], 'eobj': result[2], 'robj': result[3],
                           'error': ' Assign an HR first !','user':user})
            '''elif not res2 and desig_cd not in ('PM'):
            print('case 3')
            print(str(res1)+desig_cd)
            logged_in = request.session['eid']
            user = Employee.objects.get(e_id=logged_in)
            result = default_allocate_view()
            return render(request, 'ultimatix/admin/allocate.html',
                          {'pobj': result[0], 'dobj': result[1], 'eobj': result[2], 'robj': result[3],
                           'error': ' Please assign a manager for the project !','user':user})'''
            '''elif res1:
            # if project already have an HR
            logged_in = request.session['eid']
            user = Employee.objects.get(e_id=logged_in)
            result = default_allocate_view()
            return render(request, 'ultimatix/admin/allocate.html',
                          {'pobj': result[0], 'dobj': result[1], 'eobj': result[2], 'robj': result[3],
                           'error': ' Project already has an HR !','user':user})'''
        else:

            ob = Project_members.objects.create(pid=Project.objects.get(pid=pid),
                                            eid=Employee.objects.get(e_id=eid),
                                            rid=Project_roles.objects.get(r_id=rid),
                                            pmsdate=sdate,pmstatus='Y')
            ob.save()
            logged_in = request.session['eid']
            user = Employee.objects.get(e_id=logged_in)
            result=default_allocate_view()
            return render(request,'ultimatix/admin/allocate.html',{'pobj': result[0], 'dobj': result[1], 'eobj': result[2], 'robj': result[3],'success':' Data saved successfully !','user':user})
    else:
        try:
            logged_in = request.session['eid']
        except:
            logged_in = False
        if logged_in:
            user=Employee.objects.get(e_id=logged_in)
            result=default_allocate_view()
            return render(request,'ultimatix/admin/allocate.html',{'pobj': result[0], 'dobj': result[1], 'eobj': result[2], 'robj': result[3],'user':user})
        else:
            request.session['eid'] = None
            return redirect('ultimatix:show_login')

def default_allocate_view():
    pobj = Project.objects.all().exclude(pstatus='C')
    dobj = Designation.objects.all().exclude(d_cd='SYSADMIN')
    initial_desid=Designation.objects.all().exclude(d_cd='SYSADMIN').first().d_id
    cursor = connection.cursor()
    sql = """
    select e_id,(e_fname||" "||ifnull(e_lname,"")) from ultimatix_employee where e_id in(select es.ed_eid_id from 
    ultimatix_employee_desig es where es.ed_did_id=%s and es.ed_status='Y') and 
    e_status='Y' order by e_id
    """
    cursor.execute(sql,[initial_desid])
    res = cursor.fetchall()
    res_list = []
    for r in res:
        t={}
        #s=str(r[0])+","+str(r[1])
        #t['eid']=r[0]
        #t['ename']=r[1]
        #t.append(s)
        t['eid'] = (r[0])
        t['ename'] = (r[1])
        #t=r[0]
        res_list.append(t)
    eobj = json.dumps(res_list)
    #print('eobj:'+str(eobj))
    robj = Project_roles.objects.all().exclude(r_active='N').exclude(r_cd='OWN')
    result=[pobj,dobj,res_list,robj]
    cursor.close()
    return result


def proejctmembers_view(request,pid):
    if pid:
        if request.method=='POST':
            return HttpResponse('success')

        else:
            p=Project.objects.get(pid=pid)
            test = Project_members.objects.filter(pid=pid)
            print(test)
            #pobj=Project_members.objects.filter(pid=pid)
            cursor = connection.cursor()
            sql = """
            SELECT pm.pmid,e.e_id, (e.e_fname||" "||ifnull(e.e_lname,"")), pr.r_desc, pm.pmsdate, pm.pmedate, pm.pmstatus
            FROM ultimatix_project p
            LEFT OUTER JOIN ultimatix_project_members pm ON pm.pid_id = p.pid
            LEFT OUTER JOIN ultimatix_project_roles pr ON pr.r_id = pm.rid_id
            LEFT OUTER JOIN ultimatix_employee e ON e.e_id = pm.eid_id
            WHERE p.pid=%s order by pr.r_id DESC 
            """
            cursor.execute(sql,[pid])
            res = cursor.fetchall()
            res_list = []
            for r in res:
                t={}
                t['pmid']=str(r[0])
                t['eid']=str(r[1])
                t['name']=str(r[2])
                t['prdesc']=str(r[3])
                t['pmsdate']=str((r[4]).strftime('%Y-%m-%d  %H:%M:%S'))
                if not str(r[5]):
                    t['pmedate'] = str((r[5]).strftime('%Y-%m-%d  %H:%M:%S'))
                else:
                    t['pmedate'] = str(r[5])
                t['pmstatus']=str(r[6])
                res_list.append(t)
            #return HttpResponse(str(datetime.datetime.today().strftime('%Y-%m-%d')))
            #return HttpResponse(str(res_list))
            logged_in = request.session['eid']
            user = Employee.objects.get(e_id=logged_in)
            return render(request,'ultimatix/admin/updtprojectmembers.html',{'p':p,'res':res_list,'user':user})

    else:
        raise Http404


def mark_attendance(request):
    if request.method=='POST':
        if request.POST.get('validate'):
            adate=request.POST.get('adate')
            fname=request.FILES["myFile"]
            ext = os.path.splitext(fname.name)[1]
            if ext.lower() in ['.xlsx']:
                wb = openpyxl.load_workbook(fname)
                worksheet = wb.worksheets[0]
                try:
                    excel_list=[]
                    for i in range(1,worksheet.max_row+1):
                        if i==1:
                            continue
                        data_list={}
                        data_list['eid']=str(worksheet.cell(row=i,column=1).value)
                        data_list['swipes']=str(worksheet.cell(row=i,column=2).value)
                        ip = str(worksheet.cell(row=i, column=2).value)
                        temp = ip.split(',')
                        l = len(temp)
                        if l % 2 != 0:
                            temp.pop(-1)
                        temp_time_hldr = []
                        for i in temp:
                            datetime_object = datetime.strptime(i, '%H:%M')
                            temp_time_hldr.append(datetime_object)
                            odd_place = temp_time_hldr[::2]
                            even_place = temp_time_hldr[1:][::2]
                            total = []
                            for i, j in zip(even_place, odd_place):
                                diff = i - j
                                total.append(diff)
                            total_time = datetime(1900, 1, 1, 0, 0)
                            for i in total:
                                total_time = total_time + i
                        data_list['total_working']=total_time.strftime('%H:%M')
                        hours, minutes = (total_time.strftime('%H:%M')).split(':')
                        tot=int(hours) * 60 + int(minutes)
                        if tot>=(9*60):
                            data_list['attendance']='P'
                        elif tot>=(4.5*60):
                            data_list['attendance'] = 'H'
                        else:
                            data_list['attendance'] = 'A'
                        excel_list.append(data_list)
                        #print('adate : '+adate)
                        temp=Timesheet.objects.filter(eid=Employee.objects.get(e_id=data_list['eid']),tdate=adate)
                        if not temp:
                            ob=Timesheet.objects.create(eid=Employee.objects.get(e_id=data_list['eid']),tdate=adate,thours=data_list['total_working'],tstate=data_list['attendance'])
                            ob.save()
                        else:
                            Timesheet.objects.filter(eid=Employee.objects.get(e_id=data_list['eid']), tdate=adate).update(thours=data_list['total_working'],tstate=data_list['attendance'])

                    return render(request,'ultimatix/upload_attendance.html',{'adate':adate,'excel_list':excel_list})
                except Exception as e:
                    print('Exception : '+str(e))
                    return render(request, 'ultimatix/attendance.html', {'error': ' Some error occured while processing the data !','e':e})
                #return redirect('ultimatix:upload_attendance', adate)
            else:
                return render(request, 'ultimatix/attendance.html',{'error':' Invalid File Format !'})
        elif request.POST.get('submit'):
            return HttpResponse('sumbit')
    else:
        return render(request,'ultimatix/attendance.html')



def upload_attendance(request,adate):
    return render(request,'ultimatix/upload_attendance.html',{'adate':adate})


def apply_leave(request):
    if request.method=='POST':
        if request.POST.get('submit'):
            eid=request.session['eid']
            sdate=datetime.strptime(request.POST.get('sdate'), '%m/%d/%Y').strftime('%Y-%m-%d')
            edate = datetime.strptime(request.POST.get('edate'), '%m/%d/%Y').strftime('%Y-%m-%d')
            nof=float(request.POST.get('nof'))
            ltype=request.POST.get('leave_select')
            desc = request.POST.get('rsn')
            status='P'
            reqdate = str(datetime.now().strftime('%Y-%m-%d'))
            queueid = findqueueid(eid)

            '''Leave.objects.create(eid=Employee.objects.get(e_id=eid),sdate=sdate,edate=edate,nof=nof,
                                 ltype=ltype,desc=desc,status=status,reqdate=reqdate)
            if ltype=='0':
                rem=(Employee.objects.get(e_id=eid).e_cl)-nof
                Employee.objects.filter(e_id=eid).update(e_cl=rem)
            elif ltype=='1':
                rem=(Employee.objects.get(e_id=eid).e_sl)-nof
                Employee.objects.filter(e_id=eid).update(e_sl=rem)
            elif ltype=='2':
                rem=(Employee.objects.get(e_id=eid).e_el)-nof
                Employee.objects.filter(e_id=eid).update(e_el=rem)
            elif ltype=='3':
                rem=(Employee.objects.get(e_id=eid).e_fl)-nof
                Employee.objects.filter(e_id=eid).update(e_fl=rem)'''


            print('going queue : '+str(queueid))
            logged_in = request.session['eid']
            user=Employee.objects.get(e_id=logged_in)
            return render(request,'ultimatix/applyleave.html',{'user':user,'success':'Leave request submitted !'})


            #return HttpResponse(queueid)
    else:
        try:
            logged_in = request.session['eid']
        except:
            logged_in = False
        if logged_in:
            user=Employee.objects.get(e_id=logged_in)
            return render(request,'ultimatix/applyleave.html',{'user':user})
        else:
            request.session['eid'] = None
            return redirect('ultimatix:show_login')

def findqueueid(eid):
    ob=Project_members.objects.filter(eid_id=eid,pmstatus='Y')
    if not ob:
        print('unallocated going to admin : 1022890')
        return '1022890'
    title=Project.objects.get(pid=Project_members.objects.get(eid_id=eid,pmstatus='Y').pid_id).ptitle
    #print('title: '+title)
    if title=='TCS - MNG':
        print('going to admin : 1022890')
        return '1022890'
    else:
        pid= Project_members.objects.get(eid_id=eid,pmstatus='Y').pid_id
        hreid=Project_members.objects.get(rid_id=Project_roles.objects.get(r_cd='MNG').r_id,pid_id=pid, pmstatus='Y').eid_id
        #print(str(hreid)+" "+str(eid))
        if str(hreid)==str(eid):
            hrmeid=Employee_desig.objects.get(ed_did_id=Designation.objects.get(d_cd='HR-M').d_id,
                                              ed_status='Y').ed_eid_id
            print('going to hr manager : '+str(hrmeid))
            return hrmeid
        else:
            pmeid=Project_members.objects.get(rid_id=Project_roles.objects.get(r_cd='PM').r_id, pid_id=pid,
                                        pmstatus='Y').eid_id
            if str(pmeid)==str(eid):
                print('going to hr : '+str(hreid))
                return hreid
            else:
                print('going to pm : '+str(pmeid))
                return pmeid



def generate_payslip(request):

    try:
        logged_in = request.session['eid']
    except:
        logged_in = False
    if logged_in:
        user = Employee.objects.get(e_id=logged_in)
        return render(request, 'ultimatix/payslip.html', {'user': user})
    else:
        request.session['eid'] = None
        return redirect('ultimatix:show_login')


def calendar_view(request):
    user=Employee.objects.get(e_id=config.eid)
    return render(request,'ultimatix/calendar.html',{'user':user})
'''def deallocate_view(request,pmid):
    if pmid:
        return render(request,'ultimatix/admin/deallocate.html',{'pmid':pmid})'''

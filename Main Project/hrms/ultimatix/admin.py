from django.contrib import admin
from .models import *


# Register your models here.

class Designation_admin(admin.ModelAdmin):
    list_display = ['d_id', 'd_cd', 'd_desc', 'd_min', 'd_max', 'd_role']


admin.site.register(Designation, Designation_admin)


class Project_rolesadmin(admin.ModelAdmin):
    list_display = ['r_id', 'r_cd', 'r_desc', 'r_active', 'r_updt']


admin.site.register(Project_roles,Project_rolesadmin)


class Employee_admin(admin.ModelAdmin):
    list_display=['e_id','e_fname','e_lname','e_sname','e_dob','e_bgroup','e_mstatus','e_nationality','e_disb','e_gender','e_paddr1','e_paddr2','e_paddr3','e_caddr1','e_caddr2','e_caddr3','e_email','e_mnumber','e_doj','e_qfn','e_prev_exp','e_prev_cmp','e_cl','e_sl','e_el','e_fl','e_status','e_pwd']

admin.site.register(Employee,Employee_admin)

class id_select_admin(admin.ModelAdmin):
    list_display = ['id_desc','id_val']

admin.site.register(id_select,id_select_admin)

class Employee_desig_admin(admin.ModelAdmin):
    list_display = ['ed_id','ed_eid','ed_did','ed_sdate','ed_edate','ed_status']

admin.site.register(Employee_desig,Employee_desig_admin)

class Employee_sal_admin(admin.ModelAdmin):
    list_display = ['es_id', 'es_eid', 'es_ctc', 'es_sdate', 'es_edate', 'es_status']

admin.site.register(Employee_sal,Employee_sal_admin)


class Project_admin(admin.ModelAdmin):
    list_display = ['pid','ptitle','pdesc','psdate','pexpedate','pedate','pcrtd','pclient','pcloc','pcomplexity','ptype','pbudget','powner','pstatus']

admin.site.register(Project,Project_admin)

class Project_members_admin(admin.ModelAdmin):
    list_display = ['pmid','pid','eid','rid','pmsdate','pmedate','pmstatus']

admin.site.register(Project_members,Project_members_admin)

class Timesheet_admin(admin.ModelAdmin):
    list_display = ['tid','eid','tdate','thours','tstate']

admin.site.register(Timesheet,Timesheet_admin)

class Leave_admin(admin.ModelAdmin):
    list_display = ['lid','eid','sdate','edate','nof','ltype','status','desc','reqdate','remarks','queueid','updtby']

admin.site.register(Leave,Leave_admin)
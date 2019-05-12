from django.urls import path
from . import views
app_name='ultimatix'

urlpatterns=[
path('home/',views.home_view,name='home_view'),
path('admin/designation/',views.designation_view,name='desig_mngt'),
path('admin/roles/',views.roles_view,name='roles_mngt'),
path('admin/regemp/',views.regemp_view,name='register_emp'),
path('admin/viewemp/',views.viewemp_view,name='view_emp'),
path('admin/viewemp/<int:pk>',views.updtemp_view,name='updt_emp'),
path('admin/createproject/',views.crtprj_view,name='create_project'),
path('admin/viewprojects/',views.proejcts_view,name='view_project'),
path('admin/viewprojects/<int:pid>',views.proejctmembers_view,name='project_members'),
path('admin/viewprojects/updt/<int:pid>',views.updtproj_view,name='updt_project'),
path('admin/allocate/',views.allocate_view,name='emp_allocate'),
#path('admin/deallocate/<int:pmid>',views.deallocate_view,name='emp_deallocate'),
path('ultimatix/attendance/',views.mark_attendance,name="mark_attendance"),
path('ultimatix/attendance/<str:adate>',views.upload_attendance,name="upload_attendance"),
path('ultimatix/applyleave/',views.apply_leave,name="apply_leave"),
path('ultimatix/leaverequest/',views.leave_request,name="leave_request"),
path('ultimatix/calendar/',views.calendar_view,name="calendar_view"),
path('ultimatix/payslip/',views.generate_payslip,name="generate_payslip"),
path('ultimatix/newsfeed/',views.news_feed,name='news_feed'),
path('',views.show_login,name="show_login"),


]
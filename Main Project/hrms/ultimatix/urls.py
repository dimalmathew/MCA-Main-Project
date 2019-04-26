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
path('admin/create_project/',views.crtprj_view,name='create_project'),
path('admin/viewprojects',views.proejcts_view,name='view_project'),
path('admin/viewprojects/updt/<int:pid>',views.updtproj_view,name='updt_project'),
path('admin/allocate/',views.allocate_view,name='emp_allocate'),
path('',views.show_login,name="show_login"),
#path('admin/viewemp/updt/<int:pk>/',views.updtemp_view,name='updt_emp'),
]
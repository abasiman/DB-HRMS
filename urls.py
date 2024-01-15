from django.urls import path
from . import views
from . import manipulation, Payroll_Manipulation, Manipulation_Perfomance, department_manipulation, Leave_manipulation, Attendance_Manipulation

urlpatterns = [


      path('', views.Dashboard, name='Dashboard'),
 

    path('LeaveRequest.html/', views.LeaveRequest, name='LeaveRequest'),
    path('fillleaverecord/', views.fillleaverecord, name='fillleaverecord'),
   
    
    path('payroll_form.html/', views.payroll_form, name='payroll_form'),
    path('add_payroll/', views.add_payroll, name='add_payroll'),


   
    path('payroll_update.html/',
         Payroll_Manipulation.payroll_update, name='payroll_update'),
    path('update_payroll/<int:payroll_id>/',
         Payroll_Manipulation.update_payroll, name='update_payroll'),





    path('remove_payroll.html/',
         Payroll_Manipulation.remove_payroll, name='remove_payroll'),
    path('payroll_removal/', Payroll_Manipulation.payroll_removal,
         name='payroll_removal'),

    path('payroll/list/', Payroll_Manipulation.view_payroll_list, name='payroll_list'),



     #DEPARMENT SECTION
    path('remove_department.html/',department_manipulation.remove_department, name="remove_department"),
    path('department_removal/', department_manipulation.department_removal,
         name='department_removal'),



    path('department/list/', department_manipulation.view_department_list,
         name='Department_list'),
    path('new_department.html/', views.new_department, name="new_department"),
    path('add_department/', views.add_department, name='add_department'),

    path('update_department/<int:department_code>/',
         department_manipulation.update_department, name='update_department'),
    path('department_update.html/',department_manipulation.department_update, name="department_update"),


   
    #LEAVE SECTION
    path('Leave/list/', Leave_manipulation.view_Leave_list, name='Leave_list'),

    path('update_Leave/<int:leave_code>/',
         Leave_manipulation.update_Leave, name='update_Leave'),
    path('Leave_update.html/',Leave_manipulation.Leave_update, name="Leave_update"),

     path('remove_leave.html/',
          Leave_manipulation.remove_leave, name='remove_leave'),
    path('leave_removal/', Leave_manipulation.leave_removal,
         name='leave_removal'),




    #PEFROMANCE SECTION 
    path('performance_update.html/',
         Manipulation_Perfomance.performance_update, name='performance_update'),
    path('update_performance/<int:perfomance_id_search>/',
         Manipulation_Perfomance.update_performance, name='update_performance'),
    path('remove_perfomance.html/',
         Manipulation_Perfomance.remove_perfomance, name='remove_perfomance'),
    path('perfomance_removal/', Manipulation_Perfomance.perfomance_removal,
         name='perfomance_removal'),
         
    path('Performance/List/', Manipulation_Perfomance.view_performance_list,
         name='Performance_List'),
    

    


    #ATTENDANCE SECTION

    path('Attendance.html/', views.Attendance, name='Attendance'),
    path('recordAttendance/', views.recordAttendance, name='recordAttendance'),

    path('perfomance_table.html/', views.perfomance_table, name='perfomance_table'),
    path('recordPerformance/', views.recordPerformance, name='recordPerformance'),

     path('attendance/list/', Attendance_Manipulation.view_attendance_list, name='attendance_list'),
    path('update_attendance/<int:attendance_code>/',
         Attendance_Manipulation.update_attendance, name='update_attendance'),
    path('attendance_update.html/',
         Attendance_Manipulation.attendance_update, name="attendance_update"),
     
     path('attendance_removal.html/',
          Attendance_Manipulation.attendance_removal, name='attendance_removal'),
    path('remove_attendance/', Attendance_Manipulation.remove_attendance,
         name='remove_attendance'),
  

   

  

  #EMPLOYEE SECTION


    path('employee/list/', manipulation.view_employee_list, name='employee_list'),


    path('employeepage.html/', views.employeepage, name='employeepage'),
    path('insertemployee/', views.insertemployee, name='insertemployee'),

    path('employee_search.html/', manipulation.search_employee, name="employee_search"),
    path('employee_search.html/',
         manipulation.search_employee, name="employee_search"),
    path('employee/search/', manipulation.search_employee, name='employee_search'),
    path('employee/search/results/', manipulation.search_results,
         name='employee_search_results'),





    path('remove_employee/', manipulation.remove_employee, name='remove_employee'),
    path('empl_removal.html/', manipulation.empl_removal, name='empl_removal'),





     path('update_employee/<int:employee_id>/',manipulation.update_employee, name='update_employee'),
     path('update_employee.html/', manipulation.employee_update, name='employee_update'),



 

   


]


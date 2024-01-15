

from django.shortcuts import get_object_or_404
from .models import PayrollModel

from django.shortcuts import render, redirect
from .models import Employee
from django.http import QueryDict

from django.shortcuts import render, get_object_or_404
from .models import Department
from django.shortcuts import render
 
import json
from django.views.decorators.csrf import csrf_exempt

from django.http import JsonResponse
from django.shortcuts import render
from django.shortcuts import render, HttpResponse,redirect
from .models import LeaveRecord
from .models import EAttendance


from django.views.decorators.csrf import csrf_exempt
import json

from .models import PerfomanceTable
# Create your views here.

def Dashboard(request):
    return render(request, "Dashboard.html")

def employeepage(request):
    return render(request, "employeepage.html", {})

def Home(request):
    return render(request, "Home.html", {})


def employeepage(request):
    return render(request, "employeepage.html", {})

@csrf_exempt
def insertemployee(request):
    if request.method == "POST":
        storeId = request.POST['tuid']
        storefname = request.POST['tfname']
        storelname = request.POST['tlname']
        storeinfo = request.POST['tucontact']
        storedate = request.POST['tudate']
        storedepartment = request.POST['tudepartment']
        storejob = request.POST['tujob']

        employee_instance = Employee(
            EmployeeID=storeId,
            FirstName=storefname,
            LastName=storelname,
            ContactInfo=storeinfo,
            HireDate=storedate,
            Department=storedepartment,
            JobTitle=storejob
        )
        employee_instance.save()

    # Redirect to the "Home" page after the form is submitted
    return JsonResponse({'message': 'Attendance recorded successfully!'})


def payroll_form(request):
    return render(request, 'payroll_form.html', {})

# views.py


@csrf_exempt
def add_payroll(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            payrollID = data.get('payrollID')
            eid = data.get('eid')

            print(f"Attempting to add payroll entry for employee ID: {eid}")

            
            employee = get_object_or_404(Employee, EmployeeID=eid)

            salary = data.get('salary')
            payment_frequency = data.get('paymentFrequency')
            tax_information = data.get('taxInformation')
            deductions = data.get('deductions')

            # Create a new PayrollModel object and save it to the database
            payroll_entry = PayrollModel(
                PayrollID=payrollID,
                Eid=eid,
                Salary=salary,
                Payment_Frequency=payment_frequency,
                Tax_Information=tax_information,
                Deductions=deductions
            )
            payroll_entry.save()

            print("Payroll entry added successfully!")

            return JsonResponse({'message': 'Payroll entry added successfully!'})
        except Employee.DoesNotExist:
            print("Employee ID does not exist.")
            return JsonResponse({'message': 'This employee ID does not exist.'}, status=400)
        except Exception as e:
            print(f'Error adding payroll entry: {e}')
            return JsonResponse({'message': f'Error adding payroll entry: {e}'}, status=500)
    else:
        return render(request, 'payroll/add_payroll.html')







def Attendance(request):
    return render(request, "Attendance.html", {})


#decorator to exempt CSRF protection for simplicity in this example. In a production environment, you should handle CSRF properly.
@csrf_exempt
def recordAttendance(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            employee_id = data.get('employeeID')

            print(
                f"Attempting to add attendance record for employee ID: {employee_id}")

            # Check if the employee ID exists in the Employee table
            employee = get_object_or_404(Employee, EmployeeID=employee_id)

            attend_id = data.get('attendID')
            date = data.get('date')
            check_in_time = data.get('checkInTime')
            check_out_time = data.get('checkOutTime')

            # Create a new EAttendance object and save it to the database
            attendance_record = EAttendance(
                atEmployeeID=employee_id,
                attendID=attend_id,
                date=date,
                checkintime=check_in_time,
                checkouttime=check_out_time
            )
            attendance_record.save()

            print("Attendance recorded successfully!")

            # Return a JSON response indicating success
            return JsonResponse({'message': 'Attendance recorded successfully!'})
        except Employee.DoesNotExist:
            print("Employee ID does not exist.")
            return JsonResponse({'message': 'This employee ID does not exist.'}, status=400)
        except Exception as e:
            print(f'Error recording attendance: {e}')
            return JsonResponse({'message': f'Error recording attendance: {e}'}, status=500)
    else:
        return JsonResponse({'message': 'Invalid request method'}, status=400)




def LeaveRequest(request):
    return render(request, "LeaveRequest.html", {})

@csrf_exempt
def fillleaverecord(request):
    if request.method == 'POST':
            data=json.loads(request.body)
            leaverecordID = data.get('leaverecordID')
            employeeID = data.get('employeeID')
            start_date = data.get('start_date')
            end_date = data.get('end_date')
            leave = data.get('leave')

            leave_instance=LeaveRecord(
                leaverecordID=leaverecordID,
                employeeID=employeeID,
                start_date=start_date,
                end_date=end_date,
                leave=leave

            )
            leave_instance.save()

    return JsonResponse({'message': 'Leave Request recorded successfully!'})
     
    




def perfomance_table(request):
    return render(request, "perfomance_table.html", {})


# Use this decorator to exempt CSRF verification for simplicity (for testing purposes)


@csrf_exempt

def recordPerformance(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            perform_id = data.get("performanceID")
            employee_id = data.get('employeeID')

            print(
                f"Attempting to add performance record for employee ID: {employee_id}")
            employee = get_object_or_404(Employee, EmployeeID=employee_id)
            
            date = data.get('date')
            reviewer_id = data.get('reviewerID')
            rating = data.get('rating')
            comment = data.get('comment')

            # Create a new Performance object and save it to the database
            performance_record = PerfomanceTable(
                
                employeeID=employee_id,
                performanceID=perform_id,
                date=date,
                reviewerID=reviewer_id,
                rating=rating,
                comment=comment
            )
            performance_record.save()
           

            return JsonResponse({'message': 'Performance record added successfully!'})
        except Employee.DoesNotExist:
            print("Employee ID does not exist.")
            return JsonResponse({'message': 'This employee ID does not exist.'}, status=400)
        except Exception as e:
            print(f'Error recording performance: {e}')
            return JsonResponse({'message': f'Error recording performance: {e}'}, status=500)
    else:
        return render(request, 'perfomance/perfomance_table.html')




def new_department(request):
    return render(request, "new_department.html",{})





@csrf_exempt
def add_department(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            department_code = data.get('departmentCode')
            department_name = data.get('departmentName')
           
            department_manager = data.get('departmentManager')
            kpi = data.get('KPI')

            # Create Department instance
            department_instance = Department(
                departmentCode=department_code,
                departmentName=department_name,
                
                departmentManager=department_manager,
                KPI=kpi
            )
            department_instance.save()


            return JsonResponse({'message': 'Performance record added successfully!'})
        
        except Exception as e:
            print(f'Error recording performance: {e}')
            return JsonResponse({'message': f'Error recording performance: {e}'}, status=500)
    else:
        return render(request, 'department/new_department.html')

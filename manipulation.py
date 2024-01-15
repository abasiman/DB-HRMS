

from .models import Employee  # Import your Employee model
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.urls import reverse
from .models import Employee 
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json





#Employee Section
def view_employee_list(request):
    #retrieve all employees from the database
    employee_list=Employee.objects.all()
    context={
        'employee_list': employee_list,
    }

    return render(request, 'employee_list.html', context)

def search_employee(request):
    return render(request, 'employee_search.html')


def search_results(request):
    employee_id = request.GET.get('employee_id')
    employee = None
    error_message = None

    if employee_id:
        try:
            employee = get_object_or_404(Employee, EmployeeID=employee_id)
        except Employee.DoesNotExist:
            error_message = 'Employee not found.'

    context = {
        'employee_id': employee_id,
        'employee': employee,
        'error_message': error_message,
    }

    return render(request, 'employee_search_results.html', context)


def remove_employee(request):
    if request.method == 'POST':
        employee_id = request.POST.get('employee_id')
        try:
            employee = Employee.objects.get(EmployeeID=employee_id)
            employee.delete()
            return JsonResponse({'message': 'Employee successfully removed.'}, status=204)
        except Employee.DoesNotExist:
            return JsonResponse({'error': 'Employee not found.'}, status=404)
    return JsonResponse({'error': 'Invalid request method.'}, status=400)


def empl_removal(request):
    return render(request, 'empl_removal.html')


@csrf_exempt
def update_employee(request, employee_id):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)

            employee_entry = get_object_or_404(
                Employee, EmployeeID=employee_id)

            # Update the Employee entry
            employee_entry.FirstName = data.get('tfname')
            employee_entry.LastName = data.get('tlname')
            employee_entry.ContactInfo = data.get('tucontact')
            employee_entry.HireDate = data.get('tudate')
            employee_entry.Department = data.get('tudepartment')
            employee_entry.JobTitle = data.get('tujob')

            employee_entry.save()

            return JsonResponse({'message': 'Employee entry updated successfully'})

        except Exception as e:
            return JsonResponse({'error': True, 'message': f'Error updating Employee entry: {e}'}, status=500)
    else:
        # Fetch payroll details for the specified ID
        try:
            employee_entry = Employee.objects.get(EmployeeID=employee_id)
            data = {
                'tfname': employee_entry.FirstName,
                'tlname': employee_entry.LastName,
                'tucontact': employee_entry.ContactInfo,
                'tudate': employee_entry.HireDate,
                'tudepartment': employee_entry.Department,
                'tujob': employee_entry.JobTitle,
            }
            return JsonResponse(data)
        except Employee.DoesNotExist:
            return JsonResponse({'error': True, 'message': 'employee_entry does not exist.'}, status=404)

                
def employee_update(request):
    return render(request, 'update_employee.html')






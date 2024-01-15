from django.http import HttpResponseRedirect
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.urls import reverse
from .models import Employee, Department
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.http import JsonResponse
import json


def view_department_list(request):
    Department_list = Department.objects.all()
    context = {
        'Department_list': Department_list,
    }
    return render(request, 'Department_list.html', context)

def department_update(request):
    return render(request, 'department_update.html')


@csrf_exempt
def update_department(request, department_code):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)


           
            department_entry = get_object_or_404(
                Department, departmentCode=department_code)

            # Update the Payroll entry
            department_entry .departmentName = 'departmentName'
            department_entry.departmentManager = data.get('departmentManager')
            department_entry.KPI = data.get('KPI')
           
            # Save the updated Payroll entry
            department_entry.save()


           

            return JsonResponse({'message': 'Department entry updated successfully!'})
        except Employee.DoesNotExist:
          
            return JsonResponse({'error': True, 'message': 'Department entry does not exist.'}, status=404)
        except Exception as e:
            return JsonResponse({'error': True, 'message': f'Error updating Department entry: {e}'}, status=500)
    else:
        # Fetch department details for the specified ID
        try:
            department_entry = Department.objects.get(departmentCode=department_code)
            data = {
                'departmentName': department_entry.departmentName,
                'departmentManager': department_entry.departmentManager,
                'KPI': department_entry.KPI,

            }
            return JsonResponse(data)
        except Department.DoesNotExist:
            return JsonResponse({'error': True, 'message': 'Department entry does not exist.'}, status=404)


@csrf_protect
def department_removal(request):
    if request.method == 'POST':
        dep_code= request.POST.get('departmentCode')
        try:

            department = Department.objects.get(departmentCode=dep_code)
            department.delete()
            return JsonResponse({'message': 'department successfully removed.'}, status=204)
        except Department.DoesNotExist:
            return JsonResponse({'error': 'department not found.'}, status=404)
    return JsonResponse({'error': 'Invalid request method.'}, status=400)


def remove_department(request):
    return render(request, 'remove_department.html')

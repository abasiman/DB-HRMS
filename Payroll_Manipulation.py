# views.py

from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.http import HttpResponseServerError
from django.shortcuts import render
from .models import PayrollModel
from django.shortcuts import get_object_or_404
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import PayrollModel, Employee
import json


def payroll_update(request):
    return render(request, 'payroll_update.html')


# views.py


@csrf_exempt
def update_payroll(request, payroll_id):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)

            eid = data.get('eid')

            # Check if the Employee with the given ID exists
            get_object_or_404(Employee, EmployeeID=eid)

            # Check if the Payroll entry with the given ID exists
            payroll_entry = get_object_or_404(
                PayrollModel, PayrollID=payroll_id)

            # Update the Payroll entry
            payroll_entry.Eid = eid
            payroll_entry.Salary = data.get('salary')
            payroll_entry.Payment_Frequency = data.get('paymentFrequency')
            payroll_entry.Tax_Information = data.get('taxInformation')
            payroll_entry.Deductions = data.get('deductions')

            # Save the updated Payroll entry
            payroll_entry.save()

            return JsonResponse({'message': 'Payroll entry updated successfully!'})
        except Employee.DoesNotExist:
            return JsonResponse({'error': True, 'message': 'Employee does not exist.'}, status=404)
        except PayrollModel.DoesNotExist:
            return JsonResponse({'error': True, 'message': 'Payroll entry does not exist.'}, status=404)
        except Exception as e:
            return JsonResponse({'error': True, 'message': f'Error updating payroll entry: {e}'}, status=500)
    else:
        # Fetch payroll details for the specified ID
        try:
            payroll_entry = PayrollModel.objects.get(PayrollID=payroll_id)
            data = {
                # Access Eid directly (assuming it's a string)
                'eid': payroll_entry.Eid,
                'salary': payroll_entry.Salary,
                'paymentFrequency': payroll_entry.Payment_Frequency,
                'taxInformation': payroll_entry.Tax_Information,
                'deductions': payroll_entry.Deductions,
            }
            return JsonResponse(data)
        except PayrollModel.DoesNotExist:
            return JsonResponse({'error': True, 'message': 'Payroll entry does not exist.'}, status=404)



def view_payroll_list(request):
    payroll_list = PayrollModel.objects.all()
    context = {
            'payroll_list': payroll_list,
    }
    return render(request, 'payroll_list.html', context)



@csrf_protect
def payroll_removal(request):
    if request.method == 'POST':
        payrollID = request.POST.get('payrollID')
        try:
            
            payroll = PayrollModel.objects.get(PayrollID=payrollID)
            payroll.delete()
            return JsonResponse({'message': 'Payroll successfully removed.'}, status=204)
        except PayrollModel.DoesNotExist:
            return JsonResponse({'error': 'Payroll not found.'}, status=404)
    return JsonResponse({'error': 'Invalid request method.'}, status=400)



def remove_payroll(request):
    return render(request, 'remove_payroll.html')

from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.http import HttpResponseServerError
from django.shortcuts import render
from datetime import datetime

from django.shortcuts import get_object_or_404
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import PerfomanceTable, Employee
import json


@csrf_protect
def perfomance_removal(request):
    if request.method == 'POST':
        performanceID = request.POST.get('performanceID')
        try:
            payroll = PerfomanceTable.objects.get(performanceID=performanceID)
            payroll.delete()
            return JsonResponse({'message': 'Perfomance successfully removed.'}, status=204)
        except PerfomanceTable.DoesNotExist:
            return JsonResponse({'error': 'Perfomance not found.'}, status=404)
    return JsonResponse({'error': 'Invalid request method.'}, status=400)


def remove_perfomance(request):
    return render(request, 'remove_perfomance.html')


def view_performance_list(request):
    Performance_List = PerfomanceTable.objects.all()
    context = {
        'Performance_List': Performance_List,
    }
    return render(request, 'Performance_List.html', context)








def update_performance(request, perfomance_id_search):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            performance_record=get_object_or_404(PerfomanceTable, performanceID=perfomance_id_search)
            employeeID=data.get('employeeID')
            get_object_or_404(Employee, EmployeeID=employeeID)

            performance_record.employeeID=employeeID
            date_str = data.get('date')
            if date_str:
                performance_record.date = datetime.strptime(date_str, '%Y-%m-%d')
            performance_record.reviewerID=data.get('reviewerID')
            performance_record.rating=data.get('rating')
            performance_record.comment=data.get('comment')
            performance_record.save()
            return JsonResponse({'message': 'Performance Record updated successfully!'})
        except Employee.DoesNotExist:
            return JsonResponse({'error': True, 'message': 'Employee does not exist.'}, status=404)
        except PerfomanceTable.DoesNotExist:
            return JsonResponse({'error': True, 'message': 'Performance Record does not exist.'}, status=404)
        except Exception as e:
            return JsonResponse({'error': True, 'message': f'Error updating Performance Record: {e}'}, status=500)
    else:
        try:
            performance_record = PerfomanceTable.objects.get(
                performanceID=perfomance_id_search)
            data = {
                # Access Eid directly (assuming it's a string)
                'employeeID': performance_record.employeeID,
                'date': performance_record.date,
                'reviewerID': performance_record.reviewerID,
                'rating': performance_record.rating,
                'comment': performance_record.comment,
            }
            return JsonResponse(data)
        except PerfomanceTable.DoesNotExist:
            return JsonResponse({'error': True, 'message': 'performance Record does not exist.'}, status=404)

def performance_update(request):
    return render(request, 'performance_update.html')
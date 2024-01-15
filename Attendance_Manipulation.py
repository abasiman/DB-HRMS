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
from .models import Employee, EAttendance
import json


def view_attendance_list(request):
    attendance_list = EAttendance.objects.all()
    context = {
        'attendance_list': attendance_list,
    }
    return render(request, 'attendance_list.html', context)


def attendance_update(request):
    return render(request, 'attendance_update.html')

@csrf_exempt
def update_attendance(request, attendance_code):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)

            attendance_entry = get_object_or_404(
                EAttendance, attendID=attendance_code)

            # Update the Payroll entry
            attendance_entry.atEmployeeID = data.get('employeeID')
            attendance_entry.date = data.get('date')
            attendance_entry.checkintime = data.get('checkInTime')
            attendance_entry.checkouttime = data.get('checkOutTime')
           
            attendance_entry.save()

            return JsonResponse({'Suceess': True, 'message': 'Attendance entry successfully updated.'}, status=404)
        except Exception as e:
            return JsonResponse({'error': True, 'message': f'Error updating Attendance entry: {e}'}, status=500)
    else:
        try:
            attendance_entry = EAttendance.objects.get(
                attendID=attendance_code)
            data = {
                'employeeID': attendance_entry.atEmployeeID,
                'date': attendance_entry.date,
                'checkInTime': attendance_entry.checkintime,
                'checkOutTime': attendance_entry.checkouttime,
                

            }
            return JsonResponse(data)
        except EAttendance.DoesNotExist:
            return JsonResponse({'error': True, 'message': 'Attendance entry does not exist.'}, status=404)




def remove_attendance(request):
    if request.method == 'POST':
        attendID = request.POST.get('attendID')
        try:
            attendance = EAttendance.objects.get(attendID=attendID)
            attendance.delete()
            return JsonResponse({'message': 'Attendance successfully removed.'}, status=204)
        except Employee.DoesNotExist:
            return JsonResponse({'error': 'Attendance not found.'}, status=404)
    return JsonResponse({'error': 'Invalid request method.'}, status=400)


def attendance_removal(request):
    return render(request, 'attendance_removal.html')

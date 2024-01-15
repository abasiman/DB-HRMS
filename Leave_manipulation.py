from django.http import HttpResponseRedirect
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.urls import reverse
from .models import Employee, LeaveRecord
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.http import JsonResponse
import json


def view_Leave_list(request):
    Leave_list = LeaveRecord.objects.all()
    context = {
        'Leave_list': Leave_list,
    }
    return render(request, 'Leave_list.html', context)


def Leave_update(request):
    return render(request, 'Leave_update.html')

@csrf_exempt
def update_Leave(request, leave_code):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)

            leave_entry = get_object_or_404(
                LeaveRecord, leaverecordID=leave_code)

            # Update the Payroll entry
            leave_entry.employeeID = data.get('employeeID')
            leave_entry.start_date = data.get('start_date')
            leave_entry.end_date = data.get('end_date')
            leave_entry.leave = data.get('leave')
            

            leave_entry.save()

            return JsonResponse({'Suceess': True, 'message': 'Leave entry successfully updated.'}, status=404)
        except Exception as e:
            return JsonResponse({'error': True, 'message': f'Error updating Leave entry: {e}'}, status=500)
    else:
        try:
            leave_entry = LeaveRecord.objects.get(
                leaverecordID=leave_code)
            data = {
                'employeeID': leave_entry.employeeID,
                'start_date': leave_entry.start_date,
                'end_date': leave_entry.end_date,
                'leave': leave_entry.leave,


            }
            return JsonResponse(data)
        except LeaveRecord.DoesNotExist:
            return JsonResponse({'error': True, 'message': 'Leave entry does not exist.'}, status=404)




@csrf_protect
def leave_removal(request):
    if request.method == 'POST':
        leaverecordID = request.POST.get('leaverecordID')
        try:

            LEAVE=LeaveRecord.objects.get(leaverecordID=leaverecordID)
            LEAVE.delete()
            return JsonResponse({'message': 'LeaveRecord successfully removed.'}, status=204)
        except LeaveRecord.DoesNotExist:
            return JsonResponse({'error': 'LeaveRecord not found.'}, status=404)
    return JsonResponse({'error': 'Invalid request method.'}, status=400)


def remove_leave(request):
    return render(request, 'remove_leave.html')

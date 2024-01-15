from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.contrib.auth.models import User
from django.db import models
from django import forms
from django.core.validators import MinLengthValidator, MaxLengthValidator




class Employee(models.Model):
    EmployeeID = models.CharField(max_length=10, validators=[
                                  MinLengthValidator(10), MaxLengthValidator(10)])
    FirstName = models.CharField(max_length=50)
    LastName = models.CharField(max_length=50)
    ContactInfo = models.CharField(max_length=50)
    HireDate = models.DateField()
    Department = models.CharField(max_length=50)
    JobTitle = models.CharField(max_length=50)

    class Meta:
        db_table = "Employee"






# Define the Payroll Information Model
class PayrollModel(models.Model):
    PayrollID = models.IntegerField(primary_key=True)
    Eid = models.CharField(max_length=10, validators=[
                           MinLengthValidator(10), MaxLengthValidator(10)])
    Salary = models.DecimalField(max_digits=10, decimal_places=2)
    Payment_Frequency = models.CharField(max_length=20)
    Tax_Information = models.TextField()
    Deductions = models.TextField()

    class Meta:
        db_table = 'Payroll'



class EAttendance(models.Model):
    attendID = models.IntegerField(primary_key=True)
    atEmployeeID = models.CharField(max_length=10, validators=[
                                    MinLengthValidator(10), MaxLengthValidator(10)])
    date = models.DateField()
    checkintime = models.TimeField()
    checkouttime = models.TimeField()

    class Meta:
        db_table = "EmployeeAttendance"


        

class PerfomanceTable(models.Model):
    performanceID = models.IntegerField(primary_key=True)

    employeeID = models.CharField(
        max_length=10, validators=[MinLengthValidator(10), MaxLengthValidator(10)])
    date = models.DateField()
    reviewerID = models.CharField(
        max_length=10, validators=[MinLengthValidator(10), MaxLengthValidator(10)])

    RATING_CHOICES = [
        ('1', 'Poor'),
        ('2', 'Below Expectations'),
        ('3', 'Meets Expectations'),
        ('4', 'Exceeds Expectations'),
        ('5', 'Outstanding'),
    ]

    rating = models.CharField(max_length=50, choices=RATING_CHOICES)
    comment = models.TextField()

    class Meta:
        db_table = 'Employee_Performance'


    
class LeaveRecord(models.Model):
    leaverecordID = models.IntegerField(primary_key=True)
    employeeID = models.CharField(
        max_length=10, validators=[MinLengthValidator(10), MaxLengthValidator(10)],
        verbose_name='Employee ID')
    start_date = models.DateField()
    end_date = models.DateField()
    leave_type = [
        ('sick', 'Sick Leave'),
        ('vacation', 'Vacation'),
        ('personal', 'Personal Leave'),
        ('bereavement', 'Bereavement Leave'),
        ('other', 'Other'),
    ]
    leave = models.CharField(max_length=50, choices=leave_type)

    class Meta:
        db_table = 'LeaveRecord'


from django.db import models



class Department(models.Model):
    departmentCode = models.CharField(max_length=20)
    departmentName = models.CharField(max_length=50)
    
    departmentManager = models.CharField(max_length=50)
    KPI = models.CharField(max_length=50)

 

    class Meta:
        db_table = 'Departments'





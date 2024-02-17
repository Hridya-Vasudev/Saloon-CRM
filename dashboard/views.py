from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from employee.models import Employee
from client.models import Client
from appointment.models import Appointment
# Create your views here.
@login_required
def dashboard(request):
    emp=Employee.objects.filter(created_by=request.user).order_by('created_at')[0:5]
    client=Client.objects.all().order_by('date')
    customer=Appointment.objects.all().order_by('date')
    return render(request,'dashboard.html',{'emp':emp,'client':client,'customer':customer})
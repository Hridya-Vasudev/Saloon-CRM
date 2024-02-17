from django .contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from . models import Userprofile
from employee.views import *
from .forms  import SignupForm
from App.views import *
from dashboard.views import *
# Create your views here.
def register(request):
    if request.method=='POST':
        form=SignupForm(request.POST)        
        if form.is_valid():
            user=form.save()
            Userprofile.objects.create(user=user)
            return redirect('add_employee')            
    else:
       form=SignupForm()
    return render(request,'register.html',{'form':form})
    

@login_required(login_url='/client_list/')
def employee_only_view(request):
    # Only accessible to employees
    return render(request, 'client_list.html')

@login_required(login_url='/Appindex/')
def admin_only_view(request):
    # Only accessible to admins
    return render(request, 'index.html')
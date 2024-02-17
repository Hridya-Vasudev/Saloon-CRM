from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect,get_object_or_404
from . forms import AddEmployeeForm
from . models import Employee


@login_required
def view_employee(request):
   emp=Employee.objects.filter(created_by=request.user)
   emp=Employee.objects.filter(created_by=request.user)
   return render(request,'list_employee.html',{'emp':emp})

@login_required
def delete_employee(request,pk):
    emp=get_object_or_404(Employee,created_by=request.user,pk=pk)
    emp.delete()
    messages.success(request,'Employee is  deleted')
    return redirect('view_employee')

@login_required
def update_employee(request,pk):
    emp=get_object_or_404(Employee,created_by=request.user,pk=pk)
    if request.method == 'POST':
        form = AddEmployeeForm(request.POST,instance=emp)
        if form.is_valid():
            form.save()
            messages.success(request,'Employee is  updated')
            return redirect('view_employee')        
    else:
         form=AddEmployeeForm(instance=emp)

    return render(request,'update_employee.html',{'form':form})
  

@login_required
def add_employee(request):
    if request.method == 'POST':
        form = AddEmployeeForm(request.POST)
        if form.is_valid:
            emp=form.save(commit=False)
            emp.created_by=request.user
            emp.save()
            messages.success(request,'Employee is  created')
            return redirect('dashboard')            
    else:
        form=AddEmployeeForm()
    return render(request,'add_employee.html',{'form':form})


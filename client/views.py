from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from . models import Client
from .forms import AddClientForm
from appointment.models import Appointment
# Create your views here.
@login_required
def client_list(request):
    client=Client.objects.all()
    customer=Appointment.objects.all()
    return render(request, 'client_list.html',{'client':client,'customer':customer})

@login_required
def client_delete(request,id):
    client=Client.objects.get(id=id)    
    client.delete()
    messages.success(request,'Client is  deleted')
    return redirect('client_list')

@login_required
def convert_customer(request,id):
     customer=Appointment.objects.get(id=id)
     client=Client.objects.create(
         name=customer.first_name,
         phonenumber=customer.phone_number,
         date=customer.date,
         service=customer.service.name
     )
     customer.convert_customer=True
     customer.save()
     client.save()
     customer.delete()
     messages.success(request,'Customer is  changed to client')
     return redirect('client_list')

@login_required
def add_client(request):
    if request.method == 'POST':
        form = AddClientForm(request.POST)
        if form.is_valid:
            client=form.save(commit=False)
            client.created_by=request.user
            client.save()
            messages.success(request,'Client is  Added')
            return redirect('client_list')
    else:
     form=AddClientForm()
    return render(request,'add_client.html',{'form':form})
from .models import Service,Appointment
from django.shortcuts import render, redirect
from datetime import datetime, timedelta
from django.http import JsonResponse
from .models import Appointment

# Create your views here.

def index(request):
    return render(request, 'home.html')

def aboutpage(request):
    return render(request, 'aboutpage.html')

def service(request):
    return render(request, 'service.html')

def price(request):
    return render(request, 'price.html')

def team(request):
    return render(request, 'team.html')

def open(request):
    return render(request, 'open.html')

def admins(request):
    return redirect('/login/')

def book_appointment(request):
    services = Service.objects.all()

    slots = []
    start_time = datetime.strptime("9:00 AM", "%I:%M %p")
    end_time = datetime.strptime("9:00 PM", "%I:%M %p")
    duration = timedelta(minutes=30)
    current_time = start_time
    while current_time + duration <= end_time:
        slots.append({
            "start_time": current_time.strftime("%I:%M %p"),
            "end_time": (current_time + duration).strftime("%I:%M %p")
        })
        current_time += duration
    #available_time_slots = slots
    appointment_exists = False
    slot = None
    date = None
    if request.method == 'POST':
        # Retrieve form field values
        first_name = request.POST.get('fname')
        last_name = request.POST.get('lname')
        email = request.POST.get('email')
        phone_number = request.POST.get('mob')
        date = request.POST.get('date')
        slot = request.POST.get('slot')
        request_text = request.POST.get('ans')
        service_id = request.POST.get('service')
        # Check if the slot is available
        try:
            appointment_exists = Appointment.objects.filter(date=date, slot=slot).exists()
            
        except ValueError:
            appointment_exists = False

        if not appointment_exists and slot is not None:
            # Create new appointment object
            appointment = Appointment(
                first_name=first_name,
                last_name=last_name,
                email=email,
                phone_number=phone_number,
                date=date,
                slot=slot,
                request=request_text,
                service_id=service_id,
                slot_available=False,
            )

            # Validate the appointment object
            appointment.full_clean()

            # Save the appointment object
            appointment.save()

            # Redirect the user to the success page
            return redirect('appointment:success')
        else:
            # Redirect the user to the unavailable page
            return redirect('appointment:unavailable')
        
           
    context = {
        'services': services,
        'slots': slots,
        'b_time':slot,
        'b_date':date,
    }    
    return render(request, 'appointment.html', context)

def success(request):
    return render(request, 'success.html')

def unavailable(request):
    return render(request, 'unavailable.html')

def index_value(request):
    date = request.GET.get('date')
    booked_slots = []
    if date:
        booked_slots = Appointment.objects.filter(date=date).values_list('slot', flat=True)
    return JsonResponse({'booked_slots': list(booked_slots)})


from django.contrib import admin
from . models import Service,Appointment
# Register your models here.
admin.site.register(Appointment)
admin.site.register(Service)
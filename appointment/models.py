from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator
from django.db import models
from django.utils import timezone

class Service(models.Model):
    name = models.CharField(max_length=100)
    price = models.CharField(max_length=10)

    def __str__(self):
        return self.name  

class Appointment(models.Model):
    # Existing fields
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(null=True)
    phone_number = models.CharField(max_length=20)
    date = models.DateField()
    slot=models.CharField(max_length=100,null=False)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    request = models.TextField(null=True)
    created_at=models.DateTimeField(auto_now_add=True)

    # New field for slot availability
    slot_available = models.BooleanField(default=True)
    
    def validate_future_date(value):
        if value < timezone.now().date():
            raise ValidationError("Booking date must be in the future.")

    #date = models.DateField(validators=[validate_future_date])

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

  


# Generated by Django 4.2.2 on 2023-06-13 10:34

import appointment.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0011_appointment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='date',
            field=models.DateField(validators=[appointment.models.Appointment.validate_future_date]),
        ),
    ]

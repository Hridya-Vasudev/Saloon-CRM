# Generated by Django 4.2.1 on 2023-06-07 08:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0009_alter_appointment_slot'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Appointment',
        ),
    ]

# Generated by Django 4.2.2 on 2023-06-13 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0005_remove_client_appointments_remove_client_created_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='service',
            field=models.CharField(max_length=100, null=True),
        ),
    ]

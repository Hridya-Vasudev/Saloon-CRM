from django .contrib.auth.models import User
from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

# Create your models here.
class Userprofile(models.Model):
    user=models.OneToOneField(User,related_name='userprofile',on_delete=models.CASCADE)
    def __str__(self):
        return self.user.username 
    
class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('employee', 'Employee'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    groups = models.ManyToManyField(
        Group,
        verbose_name='groups',
        blank=True,
        related_name='customuser_set',  # Add related_name argument
        related_query_name='customuser'
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name='user permissions',
        blank=True,
        related_name='customuser_set',  # Add related_name argument
        related_query_name='customuser'
    )

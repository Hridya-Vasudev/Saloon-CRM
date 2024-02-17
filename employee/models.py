from django .contrib.auth.models import User
from django.db import models

# Create your models here.
class Employee(models.Model):
    name=models.CharField(max_length=255)
    phonenumber=models.IntegerField()
    address=models.TextField()
    id_proof=models.CharField(max_length=15,null=True)
    created_by=models.ForeignKey(User,related_name='employee',on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    modified_at=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name
    
class Comment(models.Model):
    employe=models.ForeignKey(Employee,related_name='comments',on_delete=models.CASCADE)
    description=models.TextField(blank=True,null=True)
    created_by=models.ForeignKey(User,related_name='employee_comments',on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)

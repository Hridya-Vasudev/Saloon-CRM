from django import forms
from . models import Employee,Comment

class AddEmployeeForm(forms.ModelForm):
    class Meta:
        model=Employee
        fields=('name','phonenumber','id_proof','address',)


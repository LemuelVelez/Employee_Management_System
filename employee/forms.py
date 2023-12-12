from django import forms
from .models import Employee

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['firstname', 'lastname', 'middle', 'gender']

    GENDER_CHOICES = [
        ('', '-------'),
        ('M', 'Male'),
        ('F', 'Female'),
    ]

    widgets = {
        'firstname': forms.TextInput(attrs={'class': 'form-control'}),
        'lastname': forms.TextInput(attrs={'class': 'form-control'}),
        'middle': forms.TextInput(attrs={'class': 'form-control'}),
        'gender': forms.Select(choices=GENDER_CHOICES, attrs={'class': 'form-control'}),
    }

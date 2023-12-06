from django import forms
from .models import Employee

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['firstname', 'lastname', 'middle', 'gender']

    widgets = {
        'firstname': forms.TextInput(attrs={'class': 'form-control'}),
        'lastname': forms.TextInput(attrs={'class': 'form-control'}),
        'middle': forms.TextInput(attrs={'class': 'form-control'}),
        'gender': forms.Select(attrs={'class': 'form-control'}),
    }

from django.db import models

class Employee(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]

    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    middle = models.CharField(max_length=100, blank=True, null=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)

    def __str__(self):
        return f"{self.firstname} {self.lastname}"

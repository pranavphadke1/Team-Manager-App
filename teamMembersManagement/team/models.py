from django.db import models

# Create your models here.

class Member(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=50)
    
    class Role(models.TextChoices):
        Regular = 'Regular'
        Admin = 'Admin'
    
    role = models.CharField(max_length= 7, choices=Role.choices, default=Role.Regular)
    
    def __str__(self):
        return self.first_name + ' ' + self.last_name
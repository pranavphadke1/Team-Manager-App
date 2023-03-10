from django.db import models

# Create your models here.

class Member(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=50)
    
    # Maybe change to role and enum later... 
    is_admin = models.BooleanField(default=False)

    def __str__(self):
        return self.first_name + ' ' + self.last_name
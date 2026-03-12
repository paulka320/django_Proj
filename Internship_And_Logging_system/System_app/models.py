from django.db import models
from django.contrib.auth.models import AbstractUser,Group,Permission
# Create your models here.
class CustomUser(AbstractUser):
  ROLE_CHOICES = (
    ('student','student'),
    ('academic_Supervisor','academic_Supervisor'),
    ('supervisor','supervisor'),
    ('adminstrator','adminstrator'),
  )
  role = Models.CharField(max_length=20,choice=ROLE_CHOICES)
  phone = models.CharField()
  department = models.Charfield(max_length=50)
  registration_number = models.Charfield()
  
    

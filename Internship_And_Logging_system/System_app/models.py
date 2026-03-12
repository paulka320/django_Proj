from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
# Create your models here.
class CustomUser(AbstractUser):
  ROLE_CHOICES = (
    ('student', 'student'),
    ('academic_Supervisor','academic_Supervisor'),
    ('supervisor', 'supervisor'),
    ('administrator',' administrator'),
  )
  role = Models.CharField(max_length=20,choice=ROLE_CHOICES)
  phone = models.CharField()
  department = models.Charfield(max_length=50)
  registration_number = models.Charfield()
  groups = models.ManyToManyField(
    Group,
    related_name = 'customuser_set',
    blank=True,
    help_text='The groups this user belongs to.',
    verbose_name = 'groups'
  )







  
class InternshipPlacement(models.Model):
  student = models.OneToOneField(CustomUser,on_delete = models.CASCADE)
  company_name = models.CharField(max_length=20)

    

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
  user_permissions = models.ManyToManyField(
    Permission,
    related_name ='customer_set',
    blank = True,
    help_text='Specific permission for this user.',
    verbose_name ='user permissions'
  )
  def __str__(self):
    return self.username

  

  
  class Evaluation(models.Model):
    student = models.ForeignKey(CustomUser,on_delete = models.CASCADE)
    score = models.IntegerField()
    supervisor_comment = models.TextField(blank=True)
    date_evaluated = models.DateField(auto_now_add =True)

    def __str__(self):
      return f"{self.student.username}-{self.criteria.title}"







  
class InternshipPlacement(models.Model):
  student = models.OneToOneField(CustomUser,on_delete = models.CASCADE)
  company_name = models.CharField(max_length=20)
  supervisor_name = models.CharField(max_length=20)
  supervisor_email = models.EmailField()
  start_date = models.DateField()
  end_date = models.DateField()
  def __str__(self):
      return self.company_name

class WeeklyLog(models.Model):
    student = models.ForeignKey(CustomUser,on_delete = models.CASCADE)
    week_number = models.IntegerField()
    activities = models.TextField()
    challenges = models.TextField()
    solutions = models.TextField()
    date_submitted = models.DateField()
    
    def __str__(self):
        return f"Week {self.week_number} - {self.student.username}"


class
EvaluationCriteria(models.Model):
  title = 
models.CharField(max_length=20)
  description =
models.TextField()
  max_score = 
models.IntegerField()

  def_str_(self):
    return self.title

    

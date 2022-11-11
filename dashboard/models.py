from django.db import models
from django.contrib.auth.models import User
# Create your models here.

#Notes Models Function
class Notes(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    title = models.CharField(max_length = 200)
    description = models.TextField()
    
    class Meta:
        verbose_name = 'Notes'
        verbose_name_plural = 'Notes'
        
#Model for Homework section
class Homework(models.Model):
    user = models.ForeignKey(User, on_delete =models.CASCADE)
    subject = models.CharField(max_length = 50)
    title = models.CharField(max_length = 100)
    description = models.TextField()
    due = models.DateTimeField()
    is_finished =models.BooleanField(default = False)
    
# model for ToDo section
class Todo(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    title = models.CharField(max_length = 100)
    is_finished = models.BooleanField(default = False)
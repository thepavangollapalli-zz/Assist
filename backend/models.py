from django.db import models
import datetime
from django.utils import timezone

# Create your models here.
# class Queue(models.Model):
#     name = models.CharField(max_length=100)
    
#     def __str__(self):
#         return self.name

# class QueueEntry(models.Model):
#     student_name = models.CharField(max_length=100)
#     time = models.DateTimeField(default=datetime.datetime.now())
#     question = models.TextField()
#     queue = models.ForeignKey(Queue, related_name="entries")
    
#     def __str__(self):
#         return self.student_name

class Veteran(models.Model):
    name = models.CharField(max_length=100)
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female')
        )
    gender = models.CharField(max_length=1, choices = GENDER_CHOICES, default=None)
    age = models.CharField(max_length=3)
    # ssn = models.CharField(max_length=11)
    bday = models.DateField(auto_now=False, auto_now_add=False)
    problem = models.CharField(max_length=15)
    time = models.DateTimeField(default=None)
    score = models.FloatField(default=0)

    def __str__(self):
        return self.name

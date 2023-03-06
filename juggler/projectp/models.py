from django.db import models

# Create your models here.
from django.db import models

class Project (models.Model):
    projectNum = models.IntegerField();
    project = models.CharField(max_length = 50);
    deadline = models.DateTimeField();



class Task (models.Model):
    taskNum = models.IntegerField();
    task = models.CharField(max_length = 50);


from django.db import models
from django.conf import settings

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length= 255)
    description = models.TextField()
    create_date = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.name
    
class Tasks(models.Model):
    project = models.ForeignKey(Project, on_delete = models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=255)
    priority = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Client(models.Model):
    client_name = models.CharField(max_length=255)
    email=models.EmailField(max_length=20,null=True)
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    created_by = models.ForeignKey(User, related_name='clients_created', on_delete=models.CASCADE,default=1)

    def __str__(self):
        return self.client_name

class Project(models.Model):
    project_name = models.CharField(max_length=255)
    client = models.ForeignKey(Client, related_name='projects', on_delete=models.CASCADE)
    users = models.ManyToManyField(User, related_name='projects')
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    created_by = models.ForeignKey(User, related_name='projects_created', on_delete=models.CASCADE,default=1)

    def __str__(self):
        return self.project_name
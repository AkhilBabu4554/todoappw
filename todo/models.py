from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
# Create your models here


class Task(models.Model):

    Title=models.CharField(max_length=200)
    Completed=models.BooleanField(default=False)
    Content=models.TextField(blank=True,null=True)
    User=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    
    @property
    def display(self):
        return "Done" if self.Completed else"Not Done"

    def __str__(self):
        return self.Title
    
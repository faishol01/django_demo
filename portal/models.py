from django.db import models

# Create your models here.
class UserAccount(models.Model):
    username = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=100)
    age = models.IntegerField()
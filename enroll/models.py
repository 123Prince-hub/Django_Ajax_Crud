from django.db import models

# Create your models here.
class Curd(models.Model):
    name = models.CharField(max_length=70)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
from django.db import models

# Create your models here.
class User(models.Model):
    full_name = models.CharField(max_length=250, null=False)
    address = models.CharField(max_length=200, null=False)
    mobile = models.CharField(max_length=15, null=False)
    email = models.EmailField(null=False)
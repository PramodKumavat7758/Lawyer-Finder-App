from django.contrib.auth.models import AbstractUser
from django.db import models



class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('user', 'User'),
        ('lawyer', 'Lawyer'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='user')

    def is_lawyer(self):
        return self.role == 'lawyer'

    def is_user(self):
        return self.role == 'user'

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

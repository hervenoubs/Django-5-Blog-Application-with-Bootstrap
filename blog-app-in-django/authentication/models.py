from django.db import models

class UserProfile(models.Model):
    first_name = models.CharField(max_length=100, default='')
    last_name = models.CharField(max_length=100, default='')
    username = models.CharField(max_length=100, default='')
    password = models.CharField(max_length=255, default='')
    email = models.EmailField(max_length=255, unique=True, default='')


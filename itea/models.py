from django.db import models


# Create your models here.
class User(models.Model):
    email = models.CharField(max_length=40)
    password = models.CharField(max_length=40)
    name = models.CharField(max_length=20, null=True)
    surname = models.CharField(max_length=20, null=True)

    def __str__(self):
        return f'Email:{self.email} - Pssword:{self.password} - Name:{self.name} - Surname:{self.surname}'

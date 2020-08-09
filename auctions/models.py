from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class Categories(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return f"{self.id} : {self.name}"

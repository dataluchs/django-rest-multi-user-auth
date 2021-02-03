from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
import uuid

class User(AbstractUser):
  #Boolean fields to select the type of account.
  is_company = models.BooleanField(default=False)
  is_employee = models.BooleanField(default=False)
  id = models.UUIDField(primary_key=True, default=uuid.uuid4)

class Company(models.Model):
    company = models.OneToOneField(
      settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    area = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.company.username

class Employee(models.Model):
    employee = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    country = models.CharField(max_length=100)

    def __str__(self):
        return self.employee.username
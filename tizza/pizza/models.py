from typing import Callable
from django.db import models
from django.db.models.deletion import CASCADE
from user.models import UserProfile

# Create your models here.
class Pizzeria(models.Model):
    owner = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    address = models.CharField(max_length=512)
    phone = models.CharField(max_length=50)

class Pizza(models.Model):
    title = models.CharField(max_length=140)
    description = models.CharField(max_length=240)
    thumbnail_url = models.URLField()
    approved = models.BooleanField(default=False)
    creator = models.ForeignKey(Pizzeria, on_delete=models.CASCADE)

class Likes(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=CASCADE)
    pizza = models.ForeignKey(Pizza, on_delete=CASCADE)

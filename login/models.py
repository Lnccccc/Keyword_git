from django.db import models

# Create your models here.

class User(models.Model):
    user = models.CharField(max_length=100)
    password = models.IntegerField()
    def __str__(self):
        return self.user

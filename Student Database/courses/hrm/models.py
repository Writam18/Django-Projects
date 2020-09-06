from django.db import models

# Create your models here.

class Users(models.Model):

    name = models.CharField(max_length=50,unique=True)
    subtitle = models.CharField(max_length = 50)
    description = models.CharField(max_length=1000)
    timestamp = models.IntegerField()
    created_by = models.CharField(max_length = 50)

    def __str__(self):
        return f"{self.name}"

    objects = models.Manager()
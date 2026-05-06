from django.db import models

# Create your models here.
class Instructor(models.Model):
    name = models.CharField(max_length=64)
    age = models.IntegerField()
    description = models.TextField()

    def __str__(self):
        return self.name
from django.db import models

# Create your models here.
class Trainee(models.Model):
    name = models.CharField(max_length=64, null=False)
    age = models.PositiveIntegerField()
    degree = models.DecimalField(decimal_places=2, max_digits=4, null=False)

    def __str__(self):
        return self.name
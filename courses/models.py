from django.db import models

# Create your models here.
class Course(models.Model):
    title = models.CharField(max_length=64, null=False)
    code = models.CharField(max_length=10, null=False)
    track = models.CharField(max_length=64, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

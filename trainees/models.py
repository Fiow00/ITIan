from django.db import models

from courses.models import Course

# Create your models here.
class Trainee(models.Model):
    name = models.CharField(max_length=64, null=False, blank=False)
    age = models.PositiveIntegerField()
    degree = models.DecimalField(decimal_places=2, max_digits=4, null=False, blank=False)
    image = models.ImageField(upload_to="trainees", null=True, blank=True)
    course = models.ForeignKey(
        Course,
        on_delete=models.RESTRICT,
        related_name="trainees",
    )
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
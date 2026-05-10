from django import forms

from .models import Trainee
from courses.models import Course

class TraineeForm(forms.Form):
    name = forms.CharField(max_length=64)
    age = forms.IntegerField()
    degree = forms.DecimalField(decimal_places=2, max_digits=4)
    course = forms.ModelChoiceField(queryset=Course.objects.all())
    image = forms.ImageField()
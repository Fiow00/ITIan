from django import forms

from .models import Trainee
from courses.models import Course

class TraineeForm(forms.Form):
    name = forms.CharField(
        max_length=64,
        widget=forms.TextInput(attrs={
            "placeholder": "Enter trainee name",
            "style": "color: red;",
            "autofocus": True
        })
    )

    age = forms.IntegerField(
        min_value=0,
        widget=forms.NumberInput(attrs={
            "placeholder": "Enter age",
        })
    )

    degree = forms.DecimalField(
        decimal_places=2,
        max_digits=4,
        widget=forms.NumberInput(attrs={
            "placeholder": "Enter degree (e.g. 85.50)",
            "step": 0.5,
        })
    )

    course = forms.ModelChoiceField(
        queryset=Course.objects.all(),
        empty_label="Select a course"
    )

    image = forms.ImageField()
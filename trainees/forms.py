from django import forms

from .models import Trainee
from courses.models import Course

class TraineeForm(forms.ModelForm):
    class Meta:
        model = Trainee
        fields = ["name", "age", "degree", "course", "image"]

        widgets = {
            "name": forms.TextInput(attrs={
                "placeholder": "Enter trainee name",
                "class": "form-control",
                "autofocus": True,
            }),
            "age": forms.NumberInput(attrs={
                "placeholder": "Enter age",
                "class": "form-control",
            }),
            "degree": forms.NumberInput(attrs={
                "placeholder": "Enter degree (e.g. 85.5)",
                "class": "form-control",
                "step": 0.5,
            }),
            "course": forms.Select(attrs={
                "class": "form-control",
            }),
        }
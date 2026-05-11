from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from django.views import View
from django.views.generic import ListView
from django.views.generic.edit import CreateView

from .models import Trainee
from .forms import TraineeForm

class TraineeListView(ListView):
    model = Trainee
    template_name = "trainees/trainee_list.html"
    context_object_name = "trainees"


def trainee_detail(request, trainee_id):
    return render(request, "trainees/trainee_detail.html", {
        "trainee": Trainee.objects.get(id=trainee_id),
    })


class TraineeAddView(CreateView):
    model = Trainee
    template_name = "trainees/trainee_add.html"
    fields = ["name", "age", "degree", "course", "image"]
    success_url = reverse_lazy("trainee_list")


def trainee_update(request, trainee_id):
    trainee = Trainee.objects.get(id=trainee_id)

    if request.method == "POST":
        trainee.name = request.POST["name"]
        trainee.age = request.POST["age"]
        trainee.degree = request.POST["degree"]

        trainee.save()

        return redirect("trainee_detail", trainee_id = trainee.id)

    return render(request, "trainees/trainee_update.html", {
        "trainee": trainee,
    })


def trainee_delete(request, trainee_id):
    trainee = Trainee.objects.get(id=trainee_id)

    if request.method == "POST":
        trainee.delete()
        return redirect("trainee_list")

    return render(request, "trainees/trainee_delete.html", {
        "trainee": Trainee.objects.get(id=trainee_id)
    })

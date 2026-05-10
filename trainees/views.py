from django.shortcuts import render, redirect

from .models import Trainee
from .forms import TraineeForm

def trainee_list(request):
    return render(request, "trainees/trainee_list.html", {
        "trainees": Trainee.objects.all(),
    })

def trainee_detail(request, trainee_id):
    return render(request, "trainees/trainee_detail.html", {
        "trainee": Trainee.objects.get(id=trainee_id),
    })

def trainee_add(request):
    if request.method == "POST":
        form = TraineeForm(data=request.POST, files=request.FILES)

        if form.is_valid():
            name = form.cleaned_data["name"]
            age = form.cleaned_data["age"]
            degree = form.cleaned_data["degree"]
            course = form.cleaned_data["course"]
            image = form.cleaned_data["image"]

            Trainee.objects.create(
                name=name,
                age=age,
                degree=degree,
                course=course,
                image=image
            )

            return redirect('trainee_list')
    else:
        form = TraineeForm()


    return render(request, "trainees/trainee_add.html", {
        "form": form,
    })

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

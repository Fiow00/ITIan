from django.shortcuts import render, redirect

from .models import Trainee

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
        name = request.POST["name"]
        age = request.POST["age"]
        degree = request.POST["degree"]

        Trainee.objects.create(
            name=name,
            age=age,
            degree=degree
        )

        return redirect('trainee_list')

    return render(request, "trainees/trainee_add.html")

def trainee_update(request, trainee_id):
    trainee = Trainee.objects.get(id=trainee_id)

    if request.method == "POST":
        trainee.name = request.POST["name"]
        trainee.age = request.POST["age"]
        trainee.degree = request.POST["degree"]

        trainee.save()

        return redirect("trainee_detail", trainee_id = trainee.id)

    return render(request, "trainees/trainee_update.html")

def trainee_delete(request, trainee_id):
    trainee = Trainee.objects.get(id=trainee_id)

    if request.method == "POST":
        trainee.delete()
        return redirect("trainee_list")

    return render(request, "trainees/trainee_delete.html",)

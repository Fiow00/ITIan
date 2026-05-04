from django.shortcuts import render

trainees = [
    {"id": 1, "name": "ahmed"},
    {"id": 2, "name": "mohamed"},
    {"id": 3, "name": "mostafa"},
    {"id": 4, "name": "yamen"},
]

def trainee_list(request):
    return render(request, "trainees/trainee_list.html", {
        "trainees": trainees,
    })

def trainee_add(request):
    return render(request, "trainees/trainee_add.html")

def trainee_update(request, trainee_id):
    return render(request, "trainees/trainee_update.html", {
        "trainee": trainees[trainee_id - 1],
    })

def trainee_delete(request, trainee_id):
    return render(request, "trainees/trainee_delete.html", {
        "trainee": trainees[trainee_id - 1],
    })

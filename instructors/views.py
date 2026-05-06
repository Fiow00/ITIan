from django.shortcuts import render, redirect

from .models import Instructor

# Create your views here.
def instructor_list(request):
    return render(request, "instructors/instructor_list.html", {
        "instructors": Instructor.objects.all()
    })

def instructor_detail(request, instructor_id):
    return render(request, "instructors/instructor_detail.html", {
        "instructor": Instructor.objects.get(id=instructor_id)
    })

def instructor_add(request):
    if request.method == "POST":
        name = request.POST["name"]
        age = request.POST["age"]
        description = request.POST["description"]

        Instructor.objects.create(name=name, age=age, description=description)

        return redirect("instructor_list")

    return render(request, "instructors/instructor_add.html")

def instructor_update(request, instructor_id):
    instructor = Instructor.objects.get(id=instructor_id)

    if request.method == "POST":
        instructor.name = request.POST["name"]
        instructor.age = request.POST["age"]
        instructor.description = request.POST["description"]

        instructor.save()

        return redirect("instructor_detail", instructor_id=instructor.id)

    return render(request, "instructors/instructor_update.html")

def instructor_delete(request, instructor_id):
    instructor = Instructor.objects.get(id=instructor_id)

    if request.method == "POST":
        instructor.delete()

        return redirect("instructor_list")

    return render(request, "instructors/instructor_delete.html")
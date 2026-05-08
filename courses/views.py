from django.shortcuts import render, redirect

from .models import Course

def course_list(request):
    return render(request, "courses/course_list.html", {
        "courses": Course.objects.all(),
    })

def course_detail(request, course_id):
    return render(request, "courses/course_detail.html", {
        "course": Course.objects.get(id=course_id),
    })

def course_add(request):
    if request.method == "POST":
        title = request.POST["title"]
        code = request.POST["code"]
        track = request.POST["track"]

        Course.objects.create(title=title, code=code, track=track)

        return redirect("course_list")

    return render(request, "courses/course_add.html")

def course_update(request, course_id):
    course = Course.objects.get(id=course_id)

    if request.method == "POST":
        course.title = request.POST["title"]
        course.code = request.POST["code"]
        course.track = request.POST["track"]

        course.save()

        return redirect("course_detail", course_id=course.id)

    return render(request, "courses/course_update.html")

def course_delete(request, course_id):
    course = Course.objects.get(id=course_id)

    if request.method == "POST":
        course.delete()
        return redirect("course_list")

    return render(request, "courses/course_delete.html")
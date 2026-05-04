from django.shortcuts import render

courses = [
    {"id": 1, "title": "Django"},
    {"id": 2, "title": "Python"},
    {"id": 3, "title": "JavaScript"},
    {"id": 4, "title": "React"},
]

def course_list(request):
    return render(request, "courses/course_list.html", {
        "courses": courses,
    })

def course_detail(request, course_id):
    return render(request, "courses/course_detail.html", {
        "course": courses[course_id - 1],
    })

def course_add(request):
    return render(request, "courses/course_add.html")

def course_update(request, course_id):
    return render(request, "courses/course_update.html", {
        "course": courses[course_id - 1],
    })

def course_delete(request, course_id):
    return render(request, "courses/course_delete.html", {
        "course": courses[course_id - 1],
    })
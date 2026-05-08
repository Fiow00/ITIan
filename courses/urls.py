from django.urls import path

from . import views

urlpatterns = [
    path("", views.course_list, name="course_list"),
    path("<int:course_id>/", views.course_detail, name="course_detail"),
    path("add/", views.course_add, name="course_add"),
    path("update/<int:course_id>/", views.course_update, name="course_update"),
    path("delete/<int:course_id>/", views.course_delete, name="course_delete"),
]
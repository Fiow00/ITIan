from django.urls import path

from . import views

urlpatterns = [
    path("", views.instructor_list, name="instructor_list"),
    path("<int:instructor_id>/", views.instructor_detail, name="instructor_detail"),
    path("add/", views.instructor_add, name="instructor_add"),
    path("update/<int:instructor_id>/", views.instructor_update, name="instructor_update"),
    path("delete/<int:instructor_id>/", views.instructor_delete, name="instructor_delete"),
]
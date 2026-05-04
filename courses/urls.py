from django.urls import path

from . import views

urlpatterns = [
    path("", views.course_list),
    path("<int:course_id>/", views.course_detail),
    path("add/", views.course_add),
    path("update/<int:course_id>/", views.course_update),
    path("delete/<int:course_id>/", views.course_delete),
]
from django.urls import path

from . import views

urlpatterns = [
    path("", views.trainee_list),
    path("add/", views.trainee_add),
    path("update/<int:trainee_id>/", views.trainee_update),
    path("delete/<int:trainee_id>/", views.trainee_delete),
]
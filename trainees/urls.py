from django.urls import path

from . import views

urlpatterns = [
    path("", views.TraineeListView.as_view(), name="trainee_list"),
    path("<int:trainee_id>/", views.trainee_detail, name="trainee_detail"),
    path("add/", views.TraineeAddView.as_view(), name="trainee_add"),
    path("update/<int:trainee_id>/", views.trainee_update, name="trainee_update"),
    path("delete/<int:trainee_id>/", views.trainee_delete, name="trainee_delete"),
]
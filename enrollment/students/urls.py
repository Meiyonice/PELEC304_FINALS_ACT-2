from django.urls import path
from . import views

app_name = "students"

urlpatterns = [
    path("", views.student_list, name="student_list"),
    path(
        "profile/<str:student_id>/",
        views.student_profile,
        name="student_profile"
    ),
]

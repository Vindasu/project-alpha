from django.urls import path
from projects.views import (
    show_projects,
    show_create_project,
    ProjectDetailView,
)

urlpatterns = [
    path("", show_projects, name="list_projects"),
    path("<int:pk>/", ProjectDetailView.as_view(), name="show_project"),
    path("create/", show_create_project, name="create_project"),
]

from django.urls import path
from projects.views import show_projects, show_details, show_create_project

urlpatterns = [
    path("", show_projects, name="list_projects"),
    path("<int:pk>/", show_details, name="show_project"),
    path("create/", show_create_project, name="create_project"),
]

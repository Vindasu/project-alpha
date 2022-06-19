from django.urls import path
from projects.views import show_projects, show_create_project, RecipeDetailView

urlpatterns = [
    path("", show_projects, name="list_projects"),
    path("<int:pk>/", RecipeDetailView.as_view(), name="show_project"),
    path("create/", show_create_project, name="create_project"),
]

from django.urls import path
from projects.views import show_projects

urlpatterns = [path("", show_projects, name="list_projects")]

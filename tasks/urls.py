from django.urls import path
from tasks.views import show_create_task

urlpatterns = [path("create/", show_create_task, name="create_task")]

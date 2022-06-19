from django.urls import path
from tasks.views import show_create_task, show_tasks

urlpatterns = [
    path("create/", show_create_task, name="create_task"),
    path("mine/", show_tasks, name="show_my_tasks"),
]

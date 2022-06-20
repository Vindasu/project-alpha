from django.urls import path
from tasks.views import (
    show_tasks,
    TaskUpdateView,
    TaskCreateView,
)


urlpatterns = [
    # path("create/", show_create_task, name="create_task"),
    path("create/", TaskCreateView.as_view(), name="create_task"),
    path("mine/", show_tasks, name="show_my_tasks"),
    path("<int:pk>/complete/", TaskUpdateView.as_view(), name="complete_task"),
]

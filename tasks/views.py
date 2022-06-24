from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from tasks.models import Task
from django.views.generic.edit import UpdateView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.


@login_required
def show_tasks(request):
    Model = Task.objects.filter(assignee=request.user)
    context = {"tasks": Model}
    return render(request, "tasks/list.html", context)


class TaskUpdateView(UpdateView):
    model = Task
    template_name = "tasks/list.html"
    fields = ["is_completed"]
    success_url = reverse_lazy("show_my_tasks")


class TaskCreateView(CreateView, LoginRequiredMixin):
    model = Task
    template_name = "tasks/create.html"
    fields = ["name", "start_date", "due_date", "project", "assignee"]
    success_url = reverse_lazy("show_project")

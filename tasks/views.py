from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from tasks.forms import TaskForm
from django.contrib.auth.decorators import login_required
from tasks.models import Task
from django.views.generic.edit import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
class TaskUpdateView(UpdateView):
    model = Task
    template_name = "tasks/list.html"
    fields = ["is_completed"]
    success_url = reverse_lazy("show_my_tasks")


@login_required
def show_create_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.save()
            return redirect("show_projects")
    else:
        form = TaskForm()
    context = {
        "form": form,
    }
    return render(request, "projects/create.html", context)


@login_required
def show_tasks(request):
    Model = Task.objects.filter(assignee=request.user)
    context = {"tasks": Model}
    return render(request, "tasks/list.html", context)


# function views make me cry

# @login_required
# def show_update(request, pk):
#     status = Task.objects.get(is_completed=False)
#     form = TaskForm(instance=status)
#     if request.method == "POST":
#         form = TaskForm(request.POST, instance=status)
#         if form.is_valid():
#             form.save()
#             return redirect("show_my_tasks")
#         else:
#             form = TaskForm()
#     context = {"form": form}
#     return render(request, "tasks/list.html", context)

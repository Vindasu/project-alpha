from django.shortcuts import render, redirect
from projects.models import Project
from django.contrib.auth.decorators import login_required
from projects.forms import ProjectForm
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin


class ProjectDetailView(DetailView, LoginRequiredMixin):
    model = Project
    template_name = "projects/detail.html"


@login_required
def show_projects(request):
    Model = Project.objects.filter(members=request.user)
    context = {"list_projects": Model}
    return render(request, "projects/list.html", context)


@login_required
def show_create_project(request):
    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.save()
            return redirect("show_project")
    else:
        form = ProjectForm()
    context = {
        "form": form,
    }
    return render(request, "projects/create.html", context)

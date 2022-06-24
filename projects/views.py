from django.shortcuts import render, redirect
from projects.models import Project
from django.contrib.auth.decorators import login_required
from projects.forms import ProjectForm
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.


class ProjectDetailView(DetailView, LoginRequiredMixin):
    model = Project
    template_name = "projects/detail.html"


# def get_context_data(self, **kwargs):
#     context = super(ProjectDetailView, self).get_context_data(**kwargs)
#     context["tasks"] = Task.objects.all()
#     return context


# @login_required
# def show_project_details(request, pk):
#     project = Project.objects.get(pk=pk)
#     tasks = Task.objects.get(pk=pk)
#     context = {"tasks": tasks, "project": project}
#     return render(request, "projects/detail.html", context)


@login_required
def show_projects(request):
    Model = Project.objects.filter(members=request.user)
    context = {"list_projects": Model}
    return render(request, "projects/list.html", context)


# @login_required
# def show_details(request, project_id):
#     context = Project.objects.get(project_id)
#     return render(request, "projects/details.html", context, pk=project_id)


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

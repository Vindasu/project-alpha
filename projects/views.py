from django.shortcuts import render
from projects.models import Project

# Create your views here.


def show_projects(request):
    Model = Project.objects.all()
    context = {"list_projects": Model}
    return render(request, "projects/list.html", context)

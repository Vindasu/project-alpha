from django.shortcuts import render
from projects.models import Project
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required
def show_projects(request):
    Model = Project.objects.filter(members=request.user)
    context = {"list_projects": Model}
    return render(request, "projects/list.html", context)

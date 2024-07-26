from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, JsonResponse
from .models import Project, Task 

# Create your views here.
def index(request):
    return HttpResponse("Index Page")
def hello(request, username):
    return HttpResponse("<h1>Hello %s</h1>" %username)
def about(request):
    return HttpResponse("<h1>Hello about</h1>")
def projects(request):
    projects = list(Project.objects.values())
    return JsonResponse(projects, safe=False)
def tasks(request, tittle):
    task = Task.objects.get(tittle = tittle)
    return HttpResponse('task: %s' % task.tittle)


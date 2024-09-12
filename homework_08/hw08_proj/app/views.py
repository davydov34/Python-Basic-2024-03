from django.urls import reverse_lazy
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import TaskModel

# Create your views here.
def index(request):
    return render(request, template_name='index.html')

class TaskAdd(CreateView):
    model = TaskModel
    template_name = 'task_form.html'
    fields = ['title', 'task_object', 'description']
    success_url = '/'

class TaskList(ListView):
    model = TaskModel
    template_name = 'task_list.html'
    paginate_by = 10

class TaskDetailList(DetailView):
    model = TaskModel
    template_name = 'task_detail.html'
    allow_empty = False

from django.shortcuts import render
from django.views import generic

from task_manager.models import Task, Worker


def index(request):

    task_1 = Task.objects.filter(is_completed=False)[0]
    task_2 = Task.objects.filter(is_completed=False)[1]
    task_3 = Task.objects.filter(is_completed=False)[2]
    num_current_tasks = Task.objects.filter(is_completed=False).count()
    num_completed_task = Task.objects.filter(is_completed=True).count()
    num_urgent_task = Task.objects.filter(priority="urgent").count()

    context = {
        "task_1": task_1,
        "task_2": task_2,
        "task_3": task_3,
        "num_current_tasks": num_current_tasks,
        "num_completed_task": num_completed_task,
        "num_urgent_task": num_urgent_task,
    }

    return render(request, "task_manager/index.html", context=context)


class TaskListView(generic.ListView):
    model = Task
    paginate_by = 5


class TaskDetailView(generic.DetailView):
    model = Task


class WorkerListView(generic.ListView):
    model = Worker


class WorkerDetailView(generic.DetailView):
    model = Worker

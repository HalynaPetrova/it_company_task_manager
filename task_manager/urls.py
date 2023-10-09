from django.urls import path

from .views import (
    index,
    TaskListView,
    TaskDetailView,
    WorkerListView,
    WorkerDetailView,
)

urlpatterns = [

    path("", index, name="index"),

    path(
        "tasks/",
        TaskListView.as_view(),
        name="task-list"),

    path("tasks/<int:pk>/",
         TaskDetailView.as_view(),
         name="task-detail"),

    path("workers/",
         WorkerListView.as_view(),
         name="worker-list"),

    path(
        "workers/<int:pk>/",
        WorkerDetailView.as_view(),
        name="worker-detail"
    ),
]

app_name = "task_manager"

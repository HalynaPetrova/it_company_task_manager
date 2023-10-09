from django import forms
from django.contrib.auth import get_user_model

from task_manager.models import Task, Worker


class TaskForm(forms.ModelForm):
    assignees = forms.ModelMultipleChoiceField(
        queryset=get_user_model().objects.all(),
        widget=forms.CheckboxSelectMultiple,)

    class Meta:
        model = Task
        fields = "__all__"


class WorkerForm(forms.ModelForm):
    class Meta:
        model = Worker
        fields = ("username", "first_name", "last_name", "position", "email",)

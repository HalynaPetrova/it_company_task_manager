from django.contrib.auth import get_user_model
from django.test import TestCase

from task_manager.models import Position, TaskType, Task


class ModelTests(TestCase):
    def test_position_str(self):
        position = Position.objects.create(name="test")
        self.assertEquals(str(position), position.name)

    def test_task_type_str(self):
        task_type = TaskType.objects.create(name="test")
        self.assertEquals(str(task_type), task_type.name)

    def test_task_str(self):
        task_type = TaskType.objects.create(name="test")
        task = Task.objects.create(
            name="test",
            task_type=task_type,
            description="test_description",
            is_completed=True,
            deadline="2022-12-12",
            priority="test_priority",
        )

        self.assertEquals(str(task), task.name)

    def test_create_worker_position(self):
        position = Position.objects.create(name="test")
        worker = get_user_model().objects.create(
            position=position,)

        self.assertEquals(worker.position, position)


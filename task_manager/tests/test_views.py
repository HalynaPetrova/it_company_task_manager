from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from task_manager.models import Position, TaskType, Task, Worker

TASK_URL = reverse("task_manager:task-list")
WORKER_URL = reverse("task_manager:worker-list")


class PublicTaskTest(TestCase):
    def test_login_required(self):
        res = self.client.get(TASK_URL)
        self.assertNotEquals(res.status_code, 200)


class PrivetTaskTest(TestCase):
    def setUp(self) -> None:
        self.position = Position.objects.create(name="test")
        self.worker = get_user_model().objects.create_superuser(
            username="worker",
            password="123456",
            position=self.position,
        )
        self.client.force_login(self.worker)

    def test_retrieve_task(self):
        task_type = TaskType.objects.create(name="test")
        Task.objects.create(
            name="test",
            task_type=task_type,
            description="test_description",
            is_completed=True,
            deadline="2022-12-12",
            priority="test_priority",
        )
        response = self.client.get(TASK_URL)
        self.assertEquals(response.status_code, 200)
        tasks = Task.objects.all()
        self.assertEquals(
            list(response.context["task_list"]),
            list(tasks)
        )
        self.assertTemplateUsed(response, "task_manager/task_list.html")


class PublicWorkerTest(TestCase):
    def test_login_required(self):
        res = self.client.get(WORKER_URL)
        self.assertNotEquals(res.status_code, 200)


class PrivetWorkerTest(TestCase):
    def setUp(self) -> None:
        self.position = Position.objects.create(name="test")
        self.worker = get_user_model().objects.create_superuser(
            username="worker",
            password="123456",
            position=self.position,
        )
        self.client.force_login(self.worker)

    def test_retrieve_worker(self):
        position = Position.objects.create(name="test")
        get_user_model().objects.create_superuser(
            username="worker1",
            password="123456",
            position=position,
        )
        response = self.client.get(WORKER_URL)
        self.assertEquals(response.status_code, 200)
        workers = Worker.objects.all()
        self.assertEquals(
            list(response.context["worker_list"]),
            list(workers)
        )
        self.assertTemplateUsed(response, "task_manager/worker_list.html")

    def test_create_worker(self):
        position = Position.objects.create(name="2")
        form_data = {
            "username": "username5",
            "first_name": "first",
            "last_name": "last",
            "position": position,
            "email": "test@gmail.com",
        }
        self.client.post(reverse("task_manager:worker-create"), data=form_data)
        print(self.client.post(reverse("task_manager:worker-create"), data=form_data))
        # print(form_data)
        new_worker = get_user_model().objects.get(username=form_data["username"])
        # print(new_worker)
        self.assertEqual(new_worker.first_name, form_data["first_name"])
        self.assertEqual(new_worker.last_name, form_data["last_name"])
        self.assertEqual(new_worker.position, form_data["position"])
        self.assertEqual(new_worker.email, form_data["email"])

from django.test import TestCase

from task_manager.forms import WorkerForm
from task_manager.models import Position


class FormsTests(TestCase):
    def test_worker_creation_form_with_additional_fields(self):
        position = Position.objects.create(name="test")
        form_data = {
            "username": "username",
            "first_name": "first",
            "last_name": "last",
            "position": position,
            "email": "test@gmail.com",

        }
        form = WorkerForm(data=form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data, form_data)

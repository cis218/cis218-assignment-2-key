import datetime
from django.test import TestCase
from django.urls import reverse

from .models import Todo


class TodoTests(TestCase):
    """Todo Tests"""

    @classmethod
    def setUpTestData(cls):
        """Set up the test data"""
        cls.todo = Todo.objects.create(
            name="My Test Todo",
            complete_by=datetime.date.today().isoformat(),
        )

    def test_model_content(self):
        """Test model content"""
        self.assertEqual(self.todo.name, "My Test Todo")
        self.assertEqual(self.todo.complete_by, datetime.date.today().isoformat())

    def test_url_exists_at_correct_location(self):
        """Test url exists at correct location"""
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_home_page(self):
        """Test home page"""
        # Arrange
        add_url = reverse("admin:todo_todo_add")
        change_url = reverse(
            "admin:todo_todo_change", kwargs={"object_id": self.todo.pk}
        )
        delete_url = reverse(
            "admin:todo_todo_delete", kwargs={"object_id": self.todo.pk}
        )

        # Act
        response = self.client.get(reverse("home"))

        # Assert
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "home.html")
        self.assertContains(response, "My Test Todo")
        self.assertContains(response, datetime.date.today().strftime("%b %d, %Y"))
        self.assertContains(response, f'href="{add_url}"')
        self.assertContains(response, f'href="{change_url}"')
        self.assertContains(response, f'href="{delete_url}"')

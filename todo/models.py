"""
David Barnes
CIS218
08-21-22
"""
from django.db import models


class Todo(models.Model):
    """Todo Model"""

    name = models.TextField()
    complete_by = models.DateField()

    def __str__(self):
        """String representation"""
        return f"{self.name[:30]} {self.complete_by}"

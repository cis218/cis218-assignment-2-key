from django.views.generic import ListView

from .models import Todo


class TodoPageView(ListView):
    """Todo Page View"""

    model = Todo
    template_name = "home.html"

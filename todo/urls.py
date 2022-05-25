from django.urls import path
from .views import TodoPageView

urlpatterns = [path("", TodoPageView.as_view(), name="home")]

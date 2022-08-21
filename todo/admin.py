"""
David Barnes
CIS218
08-21-22
"""
from django.contrib import admin

from .models import Todo

admin.site.register(Todo)

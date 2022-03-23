from django.db import models

from notes.models.user import User


class Note(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notes', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    content = models.CharField(max_length=50)

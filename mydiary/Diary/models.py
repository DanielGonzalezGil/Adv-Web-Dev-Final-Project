from django.db import models
from django.contrib.auth.models import User

# Database layout for the Diary app


class DiaryEntry(models.Model):
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="diary_entries"
    )
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title} by {self.created_by} on {self.created_on.strftime("%Y-%m-%d")}'

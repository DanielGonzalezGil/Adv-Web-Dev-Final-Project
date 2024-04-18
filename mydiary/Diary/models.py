from django.db import models
from django.contrib.auth.models import User

# Database layout for the Diary app


class DiaryEntry(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="diary_entries"
    )
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title} by {self.user.username} on {self.date_posted.strftime("%Y-%m-%d")}'

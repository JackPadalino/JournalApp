from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User # this import imports the User model that comes with Django

class NewEntry(models.Model):
    entry_name = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    content = models.TextField()

    def __str__(self):
        return f'{self.entry_name} | {self.date_posted}'

from django.db import models
from django.utils import timezone

class Issue(models.Model):
    name = models.CharField(max_length=200)
    text = models.TextField()
    create_date = models.DateTimeField(default=timezone.now)
    approve = models.BooleanField(default=False)
    approved_day = models.DateTimeField()
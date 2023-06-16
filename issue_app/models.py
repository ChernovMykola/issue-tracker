from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Issue(models.Model):
    ISSUE_LABEL_CHOICES = (('WR', 'Work'), ('HM', 'Home'), ('SP', 'Special'))

    name = models.CharField(max_length=200)
    text = models.TextField()
    create_date = models.DateTimeField(default=timezone.now)
    labels = models.CharField(choices=ISSUE_LABEL_CHOICES, max_length=2)
    approve = models.BooleanField(default=False)
    approved_day = models.DateTimeField()

class UserProfileInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=None)
    username = models.CharField(max_length=200, default='')
    email = models.EmailField(max_length=254, default='')
    password = models.CharField(max_length=200, default='')
    confirm_password = models.CharField(max_length=200, default='')

    def __str__(self):
        return self.user.username
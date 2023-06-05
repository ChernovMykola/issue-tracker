from django.db import models
from django.utils import timezone

class Issue(models.Model):
    name = models.CharField(max_length=200)
    text = models.TextField()
    create_date = models.DateTimeField(default=timezone.now)
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
from django.shortcuts import render
from .models import Issue
from django.views.generic import (
    ListView
)

class IssueListView(ListView):
    model = Issue

    def get_queryset(self):
        issue = Issue.objects.all()
        return issue

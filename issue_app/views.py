from django.shortcuts import render
from .models import Issue
from django.views.generic import (
    ListView,
    CreateView,
    DetailView
)

class IssueListView(ListView):
    model = Issue

    def get_queryset(self):
        issue = Issue.objects.all()
        return issue

class IssueDetailView(DetailView):
    model = Issue
    template_name = 'myissue/issue_detail.html'
    context_object_name = 'issue'

class IssueCreateView(CreateView):
    model = Issue



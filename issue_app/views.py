from django.shortcuts import (
    render,
    redirect,
)
from .models import Issue
from django.views.generic import (
    ListView,
    CreateView,
    DetailView
)
from .forms import IssueForm

class IssueListView(ListView):
    model = Issue

    def get_queryset(self):
        issue = Issue.objects.all()
        return issue

class IssueDetailView(DetailView):
    model = Issue
    template_name = 'issuetemp/issue_detail.html'
    context_object_name = 'issue'

class IssueCreateView(CreateView):
    model = Issue
    form_class = IssueForm
    redirect_field_name = 'issuetemp/myissue'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)



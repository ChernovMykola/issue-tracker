from django.shortcuts import (
    render,
    redirect,
)
from django.urls import (
    reverse_lazy
)
from .models import Issue
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin
)
from django.views.generic import (
    ListView,
    CreateView,
    DetailView,
    DeleteView,

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

class DeleteIssueView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Issue
    success_url = reverse_lazy('issuetemp:myissue')

class MyIssue(ListView):
    model = Issue
    paginate_by = 5
    template_name = 'issuetemp/myissue.html'
    context_object_name = 'myissue'

    def get_queryset(self):
        if self.request.user.is_authenticated:
            issue = Issue.objects.filter(author=self.request.user)
        else:
            issue = Issue.objects.none()
        return issue




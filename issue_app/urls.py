from django.urls import (
    path,
    re_path,
)
from . import views
urlpatterns = [
    re_path('issue/', views.IssueListView.as_view(), name='issue_list'),
    re_path('myissue/', views.MyIssue.as_view(), name='myissue'),

]
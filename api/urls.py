from django.urls import path

from api.views import IssueView, IssueDetailView, IssueUpdateView

urlpatterns = [
    path('issues/', IssueView.as_view(), name='issues'),
    path('issues/<int:pk>', IssueDetailView.as_view(), name='issue'),
    path('update_issue/<int:pk>', IssueUpdateView.as_view(), name='update_issue'),
]

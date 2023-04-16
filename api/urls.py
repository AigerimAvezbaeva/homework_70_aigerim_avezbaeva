from django.urls import path

from api.views import IssueView, IssueDetailView

urlpatterns = [
    path('issues/', IssueView.as_view(), name='issues'),
    path('issues/<int:pk>', IssueDetailView.as_view(), name='issues'),
]

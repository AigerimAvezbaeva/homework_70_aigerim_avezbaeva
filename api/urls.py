from django.urls import path

from api.views import IssueView, IssueDetailView, IssueUpdateView, IssueCreateView, IssueDeleteView, ProjectsView, \
    ProjectDetailView, ProjectUpdateView, ProjectCreateView, ProjectDeleteView

urlpatterns = [
    path('issues/', IssueView.as_view(), name='issues'),
    path('issues/<int:pk>', IssueDetailView.as_view(), name='issue'),
    path('update_issue/<int:pk>', IssueUpdateView.as_view(), name='update_issue'),
    path('create_issue/', IssueCreateView.as_view(), name='create_issue'),
    path('delete_issue/<int:pk>', IssueDeleteView.as_view(), name='delete_issue'),
    path('projects/', ProjectsView.as_view(), name='projects'),
    path('projects/<int:pk>', ProjectDetailView.as_view(), name='project'),
    path('update_project/<int:pk>', ProjectUpdateView.as_view(), name='update_project'),
    path('create_project/', ProjectCreateView.as_view(), name='create_project'),
    path('delete_project/<int:pk>', ProjectDeleteView.as_view(), name='delete_project'),
]

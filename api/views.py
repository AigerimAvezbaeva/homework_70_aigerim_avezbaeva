from rest_framework import status
from rest_framework.generics import RetrieveAPIView, UpdateAPIView, CreateAPIView, DestroyAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics

from api.serializers import IssuesSerializer, ProjectsSerializer
from tracker_app.models import Issue, Project


class IssueView(APIView):
    def get(self, request, *args, **kwargs):
        objects = Issue.objects.all()
        serializer = IssuesSerializer(objects, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class IssueDetailView(RetrieveAPIView):
    queryset = Issue.objects.all()
    serializer_class = IssuesSerializer
    lookup_field = 'pk'


class IssueUpdateView(UpdateAPIView):
    queryset = Issue.objects.all()
    serializer_class = IssuesSerializer
    lookup_field = 'pk'

    def put(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = IssuesSerializer(instance, data=request.data)
        if serializer.is_valid(raise_exception=True):
            self.perform_update(serializer)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def perform_update(self, serializer):
        instance = serializer.save()
        return instance


def perform_update(serializer):
    instance = serializer.save()
    return instance


class IssueCreateView(CreateAPIView):
    queryset = Issue.objects.all()
    serializer_class = IssuesSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class IssueDeleteView(DestroyAPIView):
    queryset = Issue.objects.all()
    serializer_class = IssuesSerializer
    lookup_field = 'pk'

    def delete(self, request, *args, **kwargs):
        issue = self.get_object()
        issue_id = issue.id
        issue.delete()
        return Response({'issue_pk': issue_id}, status=status.HTTP_204_NO_CONTENT)


class ProjectsView(APIView):
    def get(self, request, *args, **kwargs):
        objects = Project.objects.all()
        serializer = ProjectsSerializer(objects, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ProjectDetailView(RetrieveAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectsSerializer
    lookup_field = 'pk'


class ProjectUpdateView(UpdateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectsSerializer
    lookup_field = 'pk'

    def put(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = ProjectsSerializer(instance, data=request.data)
        if serializer.is_valid(raise_exception=True):
            self.perform_update(serializer)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def perform_update(self, serializer):
        instance = serializer.save()
        return instance


def perform_update(serializer):
    instance = serializer.save()
    return instance


class ProjectCreateView(CreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectsSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class ProjectDeleteView(DestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectsSerializer
    lookup_field = 'pk'

    def delete(self, request, *args, **kwargs):
        project = self.get_object()
        project_id = project.id
        project.delete()
        return Response({'project_pk': project_id}, status=status.HTTP_204_NO_CONTENT)


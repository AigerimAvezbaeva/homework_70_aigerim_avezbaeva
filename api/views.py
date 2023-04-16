from rest_framework import status
from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics

from api.serializers import IssuesSerializer
from tracker_app.models import Issue


class IssueView(APIView):
    def get(self, request, *args, **kwargs):
        objects = Issue.objects.all()
        serializer = IssuesSerializer(objects, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


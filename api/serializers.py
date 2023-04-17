from rest_framework import serializers

from tracker_app.models import Type, Issue, Project, Status


class TypesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = ['name']


class IssuesSerializer(serializers.ModelSerializer):
    type = serializers.PrimaryKeyRelatedField(many=True, queryset=Type.objects.all())
    project = serializers.PrimaryKeyRelatedField(queryset=Project.objects.all())
    status = serializers.PrimaryKeyRelatedField(queryset=Status.objects.all())

    class Meta:
        model = Issue
        fields = ('summary', 'description', 'status', 'type', 'project', 'updated_at', 'is_deleted', 'deleted_at')
        read_only_fields = ('updated_at', 'is_deleted', 'deleted_at')


class ProjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('name','created_at', 'completed_at', 'description')
        read_only_fields = ('id', 'created_at')

from rest_framework import serializers

from tracker_app.models import Type, Issue


class TypesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = ['name']


class IssuesSerializer(serializers.ModelSerializer):
    type = TypesSerializer(many=True, read_only=True)

    class Meta:
        model = Issue
        fields = ('summary', 'description', 'status', 'type', 'project', 'updated_at', 'is_deleted', 'deleted_at')

    def create(self, validated_data):
        return Issue.objects.create(**validated_data)

    def update(self, instance: Issue, validated_data):
        for field, value in validated_data.items():
            setattr(instance, field, value)
        instance.save()

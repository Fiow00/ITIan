from rest_framework import serializers

class CourseSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=64)
    code = serializers.CharField(max_length=10)
    track = serializers.CharField(max_length=64)
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        return Course.objects.create(**validated_data)
from rest_framework import serializers

from trainees.models import Trainee
from courses.models import Course

class TraineeSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=64)
    age = serializers.IntegerField()
    degree = serializers.DecimalField(max_digits=4, decimal_places=2)
    image = serializers.ImageField(required=False, allow_null=True)
    course = serializers.PrimaryKeyRelatedField(queryset=Course.objects.all())
    is_active = serializers.BooleanField(default=True)

    def create(self, validated_data):
        return Trianee.objects.create(**validated_data)
from rest_framework import viewsets, status
from rest_framework.response import Response

from courses.models import Course
from .serializers import CourseSerializer

class CourseViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Course.objects.all()
        serializer = CourseSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        try:
            course = Course.objects.get(pk=pk)
        except Course.DoesNotExist:
            return Response(
                {"detail", "Course not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = CourseSerializer(course)
        return Response(serializer.data, status=status.HTTP_200_OK)
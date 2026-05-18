from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from trainees.models import Trainee
from .serializers import TraineeSerializer

class TraineeViewSet(viewsets.ViewSet):
    # permission_classes = [IsAuthenticated]

    def list(self, request):
        queryset = Trainee.objects.all()
        serializer = TraineeSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        serialzier = TraineeSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        try:
            trainee = Trainee.objects.get(pk=pk)
        except Trainee.DoesNotExist:
            return Response(
                {"detail", "Trainee not found"},
                status=status.HTTP_404_NOT_FOUND
            )
        serializer = TraineeSerializer(trainee)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request, pk=None):
        try:
            trainee = Trainee.objects.get(pk=pk)
        except Trainee.DoesNotExist:
            return Response(
                {"detail", "Trainee not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = TraineeSerializer(trainee, data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_404_BAD_REQUEST)

    def destroy(self, request, pk=None):
        try:
            trainee = Trainee.objects.get(pk=pk)
        except Trainee.DoesNotExist:
            return Response(
                {"detail", "Trainee not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        user.delete()

        return Response(
            {"message": "Trainee Deleted successfully"},
            status=status.HTTP_200_OK
        )
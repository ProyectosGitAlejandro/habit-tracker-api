# Import DRF viewsets
from rest_framework import viewsets
# Import permissions
from rest_framework.permissions import IsAuthenticated
# Import filtered
from django_filters.rest_framework import DjangoFilterBackend 
# Import models and serializers
from .models import HabitLog
from .serializers import HabitLogSerializer

class HabitLogViewSet(viewsets.ModelViewSet):
    """
    API endpoint to manage habit logs.
    Each user can only access their own logs.
    """

    serializer_class = HabitLogSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """
        Return only logs belonging to the authenticated user.
        """
        return HabitLog.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        """
        Automatically assign the authenticated user when creating logs.
        """
        serializer.save(user=self.request.user)
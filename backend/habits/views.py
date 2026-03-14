# Import Django REST Framework viewsets
from rest_framework import viewsets

# Import permission classes
from rest_framework.permissions import IsAuthenticated

# Import models and serializers
from .models import Habit
from .serializers import HabitSerializer


class HabitViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to manage their habits.

    Each authenticated user can only access their own habits.
    """

    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """
        Return only habits belonging to the authenticated user.
        """
        return Habit.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        """
        Automatically assign the authenticated user
        when creating a new habit.
        """
        serializer.save(user=self.request.user)
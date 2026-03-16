# Import Django REST Framework viewsets
from rest_framework import viewsets

# Import permission classes
from rest_framework.permissions import IsAuthenticated

# Import filters for search and ordering
from rest_framework.filters import SearchFilter, OrderingFilter

# Import DjangoFilterBackend for field filtering
from django_filters.rest_framework import DjangoFilterBackend

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

    # Enable filtering, search and ordering
    filter_backends = [
        DjangoFilterBackend,
        SearchFilter,
        OrderingFilter,
    ]

    # Allow filtering by specific fields
    filterset_fields = ["created_at"]

    # Enable search by habit name
    search_fields = ["name"]

    # Allow ordering by fields
    ordering_fields = ["created_at", "name"]

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
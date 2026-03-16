# Import Django REST Framework serializers
from rest_framework import serializers

# Import Habit model
from .models import Habit

# Import business logic functions from the services layer
# These functions handle habit streak calculations
from .services import calculate_current_streak, calculate_longest_streak


class HabitSerializer(serializers.ModelSerializer):
    """
    Serializer for the Habit model.

    This serializer converts Habit model instances into JSON format
    and includes additional computed fields such as streak metrics.

    Computed fields:
    - current_streak: number of consecutive days the habit has been completed
    - longest_streak: highest streak ever achieved for the habit
    """

    # Computed field for the current streak of the habit
    current_streak = serializers.SerializerMethodField()

    # Computed field for the longest streak achieved
    longest_streak = serializers.SerializerMethodField()

    class Meta:
        """
        Meta configuration for the serializer.

        Defines which model is used and which fields are exposed
        through the API.
        """
        model = Habit
        fields = "__all__"
        read_only_fields = ["user"]

    def get_current_streak(self, obj):
        """
        Calculate the current streak for the given habit.

        This method retrieves the authenticated user from the request
        context and delegates the streak calculation to the services layer.

        Args:
            obj (Habit): Habit instance being serialized

        Returns:
            int: Current streak value
        """

        user = self.context["request"].user
        return calculate_current_streak(obj, user)

    def get_longest_streak(self, obj):
        """
        Calculate the longest streak achieved for the habit.

        Uses the services layer to determine the maximum
        consecutive completion streak recorded.

        Args:
            obj (Habit): Habit instance being serialized

        Returns:
            int: Longest streak value
        """

        user = self.context["request"].user
        return calculate_longest_streak(obj, user)
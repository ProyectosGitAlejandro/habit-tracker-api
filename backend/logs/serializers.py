# Import DRF serializer tools
from rest_framework import serializers

# Import the HabitLog model
from .models import HabitLog


class HabitLogSerializer(serializers.ModelSerializer):
    """
    Serializer for HabitLog model.
    Converts HabitLog instances into JSON.
    """

    class Meta:
        model = HabitLog
        fields = "__all__"
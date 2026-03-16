from rest_framework import serializers


class AnalyticsSerializer(serializers.Serializer):
    """
    Serializer for user analytics metrics.

    This serializer validates and structures the analytics
    data returned by the analytics service layer.
    """

    total_habits = serializers.IntegerField()
    completed_today = serializers.IntegerField()
    completion_rate = serializers.IntegerField()
    consistency_score = serializers.IntegerField()


class HeatmapSerializer(serializers.Serializer):
    """
    Serializer for habit heatmap data.

    Each entry represents a single day and the number
    of completed habits for that date. This format allows
    the frontend to render a GitHub-style activity heatmap.
    """

    date = serializers.DateField()
    count = serializers.IntegerField()
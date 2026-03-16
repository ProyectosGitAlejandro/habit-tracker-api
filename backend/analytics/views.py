from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .services import get_user_analytics, get_user_heatmap, get_weekly_completion, get_best_habits, get_monthly_completion
from .serializers import AnalyticsSerializer, HeatmapSerializer


class AnalyticsView(APIView):
    """
    API endpoint that returns analytics statistics for the
    authenticated user.
    """

    permission_classes = [IsAuthenticated]

    def get(self, request):
        """
        Return high-level analytics metrics.
        """

        data = get_user_analytics(request.user)
        serializer = AnalyticsSerializer(data)

        return Response(serializer.data)


class HeatmapView(APIView):
    """
    API endpoint that returns habit completion data
    formatted for a heatmap visualization.
    """

    permission_classes = [IsAuthenticated]

    def get(self, request):
        """
        Return aggregated habit completion data
        for the authenticated user.
        """

        data = get_user_heatmap(request.user)
        serializer = HeatmapSerializer(data, many=True)

        return Response(serializer.data)

class WeeklyAnalyticsView(APIView):  
    """
    API endpoint that returns weekly habit completion statistics.

    This endpoint aggregates completed habits by week
    so the frontend can build productivity charts.
    """

    permission_classes = [IsAuthenticated]

    def get(self, request):
        data = get_weekly_completion(request.user)
        return Response(data)

class BestHabitsView(APIView):  
    """
    API endpoint that returns the habits with the highest completion rate.

    This allows the frontend to display the user's
    most consistent habits.
    """

    permission_classes = [IsAuthenticated]

    def get(self, request):
        data = get_best_habits(request.user)
        return Response(data)
    
class MonthlyAnalyticsView(APIView):  
    """
    API endpoint that returns monthly habit completion statistics.

    This allows the frontend to visualize long-term
    productivity trends over time.
    """

    permission_classes = [IsAuthenticated]

    def get(self, request):
        data = get_monthly_completion(request.user)
        return Response(data)
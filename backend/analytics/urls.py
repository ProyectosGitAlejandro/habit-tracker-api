from django.urls import path
from .views import AnalyticsView, HeatmapView, WeeklyAnalyticsView, BestHabitsView, MonthlyAnalyticsView


"""
URL configuration for analytics endpoints.
"""

urlpatterns = [
    path("", AnalyticsView.as_view(), name="analytics"),
    path("heatmap/", HeatmapView.as_view(), name="heatmap"),
    path("weekly/", WeeklyAnalyticsView.as_view(), name="analytics-weekly"),
    path("best-habits/", BestHabitsView.as_view(), name="analytics-best-habits"),
    path("monthly/", MonthlyAnalyticsView.as_view(), name="analytics-monthly"),
]
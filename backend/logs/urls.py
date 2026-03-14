# Import DRF router
from rest_framework.routers import DefaultRouter

# Import the viewset
from .views import HabitLogViewSet

# Create router
router = DefaultRouter()

# Register endpoint
router.register(r'logs', HabitLogViewSet, basename='logs')

# Export URLs
urlpatterns = router.urls
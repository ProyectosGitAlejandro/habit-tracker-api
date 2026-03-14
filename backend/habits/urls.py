# Import Django REST Framework router
from rest_framework.routers import DefaultRouter

# Import the Habit viewset
from .views import HabitViewSet

# Create a router instance
router = DefaultRouter()

# Register the HabitViewSet with a basename
router.register(r'habits', HabitViewSet, basename='habit')

# Export the router URLs
urlpatterns = router.urls
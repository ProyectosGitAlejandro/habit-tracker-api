# Import Django utilities to define URL routes and include other URL configurations
from django.urls import path, include

# Import JWT authentication views for login and token refresh
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


# Main URL configuration for the API
urlpatterns = [

    # Authentication endpoint
    # Allows users to obtain an access and refresh token by providing credentials
    path('api/auth/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),

    # Endpoint to refresh an expired access token using a refresh token
    path('api/auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Habit management endpoints (CRUD operations for habits)
    path('api/', include('habits.urls')),

    # Habit logs endpoints (track daily completion of habits)
    path('api/', include('logs.urls')),
]
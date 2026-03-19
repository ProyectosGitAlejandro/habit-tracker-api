# Import Django admin
from django.contrib import admin

# Import Django utilities to define URL routes and include other URL configurations
from django.urls import path, include

# Import JWT authentication views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

#Import Drf documentation 
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView


urlpatterns = [
    # Root endpoint (health check)
    path('', home),

    # Admin
    path('admin/', admin.site.urls),

    # Auth
    path('api/auth/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Apps
    path('api/habits/', include('habits.urls')),
    path('api/logs/', include('logs.urls')),
    path('api/analytics/', include('analytics.urls')),

    # API Docs
    path('api/schema/', SpectacularAPIView.as_view(), name='api-schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='api-schema'), name='api-docs'),
]
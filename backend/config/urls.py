# Import Django admin
from django.contrib import admin

# Import Django utilities to define URL routes and include other URL configurations
from django.urls import path, include

# Import JWT authentication views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

#Import Drf documentation 
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView


urlpatterns = [
    # Django admin panel
    path('admin/', admin.site.urls),
    # Authentication endpoint
    path('api/auth/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # Token refresh endpoint
    path('api/auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # Habits endpoints
    path('api/', include('habits.urls')),
    # Logs endpoints
    path('api/', include('logs.urls')),
    # Analitycs endpoints
     path("api/analytics/", include("analytics.urls")),
    #API Documentation
    path("api/schema/", SpectacularAPIView.as_view(), name="api-schema"),  # NEW
    path("api/docs/", SpectacularSwaggerView.as_view(url_name="api-schema"), name="api-docs"),  # NEW
    
]
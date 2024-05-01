from django.contrib import admin
from django.urls import path,include
from API.views import User

from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
swagger = [
    # YOUR PATTERNS
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    # Optional UI:
    path('api/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('API.urls')), #<=這裡
] + swagger

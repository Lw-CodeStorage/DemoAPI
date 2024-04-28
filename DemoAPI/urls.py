from django.contrib import admin
from django.urls import path,include
from API.views import User
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('API.urls')), #<=這裡
]

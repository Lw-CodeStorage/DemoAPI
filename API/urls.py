from django.urls import path
from .views import UserList

urlpatterns = [
    path('api/user/', UserList.as_view(), name='UserAPI'),
]
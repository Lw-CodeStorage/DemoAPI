from django.urls import path
from .views import UserList,PostList

urlpatterns = [
    path('api/post/',PostList.as_view()),
    path('api/user/', UserList.as_view(), name='UserAPI'),
    # path('api/user/<int:pk>', UserDetail.as_view(), name='UserAPI'),
]
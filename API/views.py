from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import User,Post
from .serializers import UserSerializer,PostSerializer
from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiTypes

class PostList(APIView):

    def get(self,request):
        posts = Post.objects.all()
        serializer = PostSerializer(posts,many=True)
        return Response(serializer.data)
    
    

class UserList(APIView):

    def get(self,request):
        users = User.objects.all()
        serializer =  UserSerializer(users,many=True)
        return Response(serializer.data)
    
    
    @extend_schema(
        request=UserSerializer,
    )
    def post(self,request):
        serializer = UserSerializer(data=request.data)  
        if serializer.is_valid():
            serializer.save()  
            return Response({"status": "success", "data": serializer.data}, status=200)  
        else:  
            return Response({"status": "error", "data": serializer.errors}, status=400)

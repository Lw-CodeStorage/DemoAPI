from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import User,Post
from .serializers import PostSearch,PostInsert
from .serializers import UserSerializer
from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiTypes

class PostList(APIView):

    def get(self,request):
        # posts = Post.objects.all()
        # posts = Post.objects.filter(user = 1)
        posts = Post.objects.filter(content__contains='2')
        serializer = PostSearch(posts,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer = PostInsert(data=request.data)  
        if serializer.is_valid():
            serializer.save()  
            return Response({"status": "success", "data": serializer.data}, status=200)  
        else:  
            return Response({"status": "error", "data": serializer.errors}, status=400)

class UserList(APIView):

    @extend_schema(
        parameters=[
            OpenApiParameter(
                name="query_param",
                type=OpenApiTypes.STR,
                description="一個查詢參數",
                location=OpenApiParameter.QUERY
            ),
        ]
    )
    def get(self,request):
        id = request.query_params.get('id')
        if id is not None:
            user = User.objects.get(pk=id)
            serializer =  UserSerializer(user)
        else:
            user = User.objects.all()
            serializer =  UserSerializer(user)
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


    @extend_schema(
        request=UserSerializer,
        parameters=[
            OpenApiParameter(
                required = True,
                name="query_param",
                type=OpenApiTypes.STR,
                description="一個查詢參數",
                location=OpenApiParameter.QUERY
            ),
        ]
    )
    def put(self,request):
            id = request.query_params.get('id')
            user = User.objects.get(id=id)
            serializer = UserSerializer(instance=user,data=request.data)
            if(serializer.is_valid()):
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=400)
            
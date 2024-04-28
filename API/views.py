from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import User
from .serializers import UserSerializer

class UserList(APIView):
    def get(self,request):
        users = User.objects.all()
        serializer =  UserSerializer(users,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer = UserSerializer(data=request.data)  
        if serializer.is_valid():
            test = serializer.validate()
            serializer.save()  
            return Response({"status": "success", "data": serializer.data}, status=200)  
        else:  
            return Response({"status": "error", "data": serializer.errors}, status=400)
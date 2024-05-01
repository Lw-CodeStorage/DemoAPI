from rest_framework import serializers
from .models import User,Post


class PostSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Post
        fields="__all__"
        depth = 1

class UserSerializer(serializers.ModelSerializer):

    # 反向關聯
    post = PostSerializer(many=True, read_only=True)

    # 覆寫 models的create_dt
    create_dt = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S",read_only=True)
    update_dt = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S",read_only=True)
    
    class Meta:
        model = User
        fields="__all__"
     
        
       




# class User_Post_Serialize(serializers.ModelSerializer):
    
#     # 覆寫 models的create_dt
#     create_dt = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")

#     # 反向關聯
#     post = PostSerializer(many=True, read_only=True)

#     class Meta :
#         model = User
#         fields="__all__"

# class Post_User_Serialize(serializers.ModelSerializer):

#     # 反向關聯
#     user = UserSerializer( read_only=True)

#     class Meta :
#         model = Post
#         fields="__all__"
from rest_framework import serializers
from .models import User,Post




class UserSerializer(serializers.ModelSerializer):

    # 反向關聯
    
    post = serializers.StringRelatedField(many=True, read_only=True)
    # post = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    # post = PostSerializer(many=True, read_only=True)
   
    # 覆寫 models的create_dt
    create_dt = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S",read_only=True)
    update_dt = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S",read_only=True)
    
    class Meta:
        model = User
        fields="__all__"
        depth = 1

     
        
       

class PostSerializer(serializers.ModelSerializer):
    
    # fk關聯
    # - 解析成固定欄位
    # - 要更多個可以多設定
    usermame = serializers.ReadOnlyField(source="user.name")
    category = serializers.ReadOnlyField(source="category.name")

    
    class Meta:
        model = Post
        fields="__all__"
        # depth = 1




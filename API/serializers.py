from rest_framework import serializers
from .models import User,Post



# 可以考慮取資料 與 寫資料分兩個序列化
class UserSerializer(serializers.ModelSerializer):

    # 反向關聯
    # post = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    # post = serializers.StringRelatedField(many=True, read_only=True)
    # post = PostSerializer(many=True, read_only=True)

    # 覆寫 models的create_dt
    create_dt = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S",read_only=True)
    update_dt = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S",read_only=True)
    
    class Meta:
        model = User
        fields="__all__"
        depth = 1


        
       

class PostSearch(serializers.ModelSerializer):
    
    # fk自訂關聯解析，or 使用 depth = 1 自動將關聯帶出
    usermame = serializers.ReadOnlyField(source="user.name")
    categoryname = serializers.ReadOnlyField(source="category.name")
    
    class Meta:
        model = Post
        fields="__all__"
        # depth = 1

class PostInsert(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields="__all__"

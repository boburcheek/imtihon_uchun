from .models import Post
from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username")


class PostSerializer(ModelSerializer):
    # owner = UserSerializer()

    class Meta:
        model = Post
        fields = ("id", "title", "description", "created_at", "author", "owner")
        read_only_fields = ("owner",)

    def create(self, validated_data):
        print(11111111111111111)
        print(validated_data)
        return Post.objects.create(**validated_data)

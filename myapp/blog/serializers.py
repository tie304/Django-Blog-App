from rest_framework import serializers
from .models import Post, User


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'body_text', 'pub_date']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'likes']


class UserSerializerIn(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['name']


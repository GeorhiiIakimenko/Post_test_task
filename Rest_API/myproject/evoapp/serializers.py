from rest_framework import serializers
from .models import Post, PostAnalytics, UserActivity
from django.contrib.auth.models import User


# Serializer for User model.
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'last_login']


# Serializer for Post model.
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'user', 'content', 'likes']


# Serializer for PostAnalytics model.
class PostAnalyticsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostAnalytics
        fields = ['id', 'date', 'likes_count', 'post']


class UserActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = UserActivity
        fields = ['user', 'last_activity']



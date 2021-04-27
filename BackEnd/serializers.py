from rest_framework import serializers
from .models import *


class NewsSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsSection
        fields = ("news_category", "id")

class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ("title", "category", "news_description", "date_published", "source", "url", "id")

class NewsSerializerWithNewsSectionId(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ("title", "category", "news_description", "date_published", "source", "url", "id", "category")

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ("author", "title", "date_posted", "post_description", "id")

class PostSerializerWithAuthorId(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ("author", "title", "date_posted", "post_description", "id", "author")

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ("post_id", "author", "comment_description", "date_commented", "id")

class CommentSerializerWithPostAndAuthorId(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ("post_id", "author", "comment_description", "date_commented", "id", "post_id", "author")

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password')
        extra_kwargs = {
            'password':{'write_only': True},
        }
    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'],
        password = validated_data['password'])
        return user
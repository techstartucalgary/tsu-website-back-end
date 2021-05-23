from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from .models import *

class EventSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventSection
        fields = ("event_category", "id")

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ("title", "category", "event_description", "date_published", "source", "url", "id")

class EventSerializerWithEventSectionId(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ("title", "category", "event_description", "date_published", "source", "url", "id", "category")

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
    email = serializers.EmailField(
            required=True,
            validators=[UniqueValidator(queryset=User.objects.all())]
            )

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'password')
        extra_kwargs = {
            'password':{'write_only': True},
        }
    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'],
        first_name = validated_data['first_name'],
        last_name = validated_data['last_name'],
        email = validated_data['email'],
        password = validated_data['password'])
        return user
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import status
from .models import *
from .serializers import *
from django.http import HttpResponse, response
from django.contrib.auth import get_user_model
from rest_framework import permissions
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

# Create your views here.
class saveNewsSection(generics.CreateAPIView):
    queryset = NewsSection.objects.all()
    serializer_class = NewsSectionSerializer

class getNewsSection(generics.ListAPIView):
    queryset = NewsSection.objects.all()
    serializer_class = NewsSectionSerializer

class deleteNewsSection(generics.DestroyAPIView):
    queryset = NewsSection.objects.all()
    serializer_class = NewsSectionSerializer

class updateNewsSection(generics.RetrieveUpdateAPIView):
    queryset = NewsSection.objects.all()
    serializer_class = NewsSectionSerializer

class saveNews(generics.CreateAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializerWithNewsSectionId

class getNews(generics.ListAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer

class deleteNews(generics.DestroyAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer

class updateNews(generics.RetrieveUpdateAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializerWithNewsSectionId

class savePost(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializerWithAuthorId

class getPost(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class deletePost(generics.DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class updatePost(generics.RetrieveUpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializerWithAuthorId

class saveComment(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializerWithPostAndAuthorId

class getComment(generics.ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class deleteComment(generics.DestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class updateComment(generics.RetrieveUpdateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializerWithPostAndAuthorId

class RegisterUserView(generics.CreateAPIView):
    model = get_user_model()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = RegisterSerializer 

class updateUserPost(generics.RetrieveUpdateAPIView):
    def get_queryset(self):
        queryset = Post.objects.all()
        queryset = queryset.filter(author=self.request.user)
	# Leftside of filter: from queryset. Rightside: how we're filtering
        return queryset
    serializer_class = PostSerializerWithAuthorId

class customObtainAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        response = super(customObtainAuthToken, self).post(request, *args, **kwargs)
        token = Token.objects.get(key=response.data['token'])
        return Response({'token': token.key, 'id': token.user_id})

def pingAppView(request):
    return HttpResponse("")
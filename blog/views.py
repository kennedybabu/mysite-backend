from django.shortcuts import render, get_object_or_404
from .models import Post
from rest_framework.response import Response
from rest_framework.decorators import api_view 
from .serializers import PostSerializer, UserSerializer 
from django.contrib.auth.models import User

# Create your views here.


# get user 
@api_view(['GET'])
def getUser(request, id):
    user = User.objects.get(id = id)
    serializer = UserSerializer(user, many=False)
    return Response(serializer.data)


@api_view(['GET'])
def getAllUsers(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def post_list(request):
    posts = Post.objects.all()
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)

# @api_view(['GET'])
# def getPosts(request):
#     posts = Post.objects.all()
#     serializer = PostSerializer(posts, many=True)
#     return Response(serializer.data)


@api_view(['GET'])
def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post, status='published',publish_year=year,publish_month=month,publish_day=day)
    serializer = PostSerializer(post,many=False)
    return Response(serializer.data)

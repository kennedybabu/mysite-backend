from django.shortcuts import render, get_object_or_404
from .models import Post
from rest_framework.response import Response
from rest_framework.decorators import api_view 
from .serializers import PostSerializer, UserSerializer 
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
import json
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
    # comments = post.comments.all()
    serializer = PostSerializer(post,many=False)
    return Response(serializer.data)


@api_view(['POST'])
def create_post(request):
    # post = json.loads(request.body)
    # serializer = PostSerializer(post, many=False)
    # return Response(serializer.data)
    try:
        data = json.loads(request.body)
        serializer = PostSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        else:
            return Response(serializer.errors, status=400)
    except json.JSONDecodeError:
        return Response({"error":"Invalid JSON data"}, status=400)

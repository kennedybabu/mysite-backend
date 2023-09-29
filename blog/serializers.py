from rest_framework.serializers import ModelSerializer
from .models import Post, Comment 
from django.contrib.auth.models import User



class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'



class PostSerializer(ModelSerializer):
    comments = CommentSerializer(many=True)
    class Meta:
        model = Post
        fields = ('title', 'slug', 'author', 'body', 'publish', 'created', 'updated', 'status','objects', 'published','comments',)

class UserSerializer(ModelSerializer):
    class Meta:
        model = User 
        fields = ('username',)


from rest_framework.serializers import ModelSerializer
from .models import Post, Comment 
from django.contrib.auth.models import User



class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'



class PostSerializer(ModelSerializer):
    comments = CommentSerializer(many=True, required=False)
    class Meta:
        model = Post
        fields = ('author', 'body', 'publish', 'created', 'updated','objects', 'published','comments',)

class UserSerializer(ModelSerializer):
    class Meta:
        model = User 
        fields = ('username',)


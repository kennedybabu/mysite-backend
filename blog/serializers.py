from rest_framework.serializers import ModelSerializer
from .models import Post 
from django.contrib.auth.models import User




class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = ('title', 'slug', 'author', 'body', 'publish', 'created', 'updated', 'status','objects', 'published',)

class UserSerializer(ModelSerializer):
    class Meta:
        model = User 
        fields = ('username',)
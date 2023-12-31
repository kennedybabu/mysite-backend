from rest_framework.serializers import ModelSerializer
from .models import Post, Comment 
from django.contrib.auth.models import User
from rest_framework import serializers 
from rest_framework.validators import UniqueValidator



class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'



class PostSerializer(ModelSerializer):
    comments = CommentSerializer(many=True, required=False)
    author_username = serializers.ReadOnlyField(source='author.username')
    class Meta:
        model = Post
        fields = ('id','author', 'author_username', 'body', 'publish', 'created', 'updated','objects', 'published','comments',)

class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True, validators=[UniqueValidator(queryset=User.objects.all())])
    username = serializers.CharField(validators=[UniqueValidator(queryset=User.objects.all())])
    password = serializers.CharField(min_length=8, write_only=True)

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])
        return user
    class Meta:
        model = User 
        fields = ('id','username','email', 'password',)


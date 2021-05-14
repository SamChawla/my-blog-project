from rest_framework import serializers
from blogs.models import Post


class PostListSerializer(serializers.ModelSerializer): 
    user = serializers.SerializerMethodField()
    # user_email = serializers.ReadOnlyField(source='author.email')
    
    class Meta:
        model = Post
        fields = ['id', 'title','user', 'content', 'status']
    
    def get_user(self, obj):
        return obj.author.username

class PostCreateUpdateSerializer(serializers.ModelSerializer): 
    
    class Meta:
        model = Post
        fields = ['title', 'content', 'status']
    
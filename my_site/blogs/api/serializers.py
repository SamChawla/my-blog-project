from rest_framework.serializers import ModelSerializer
from blogs.models import Post


class PostCreateUpdateSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = ["title", "content", "published_at"]


class PostDetailSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = ["id", "title", "content", "published_at"]


class PostListSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = ["id", "title", "content", "published_at"]

from blogs.models import Post
from rest_framework.generics import (
    CreateAPIView,
    DestroyAPIView,
    ListAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    RetrieveUpdateAPIView,
    )

from .serializers import (
    PostCreateUpdateSerializer,
    PostDetailSerializer,
    PostListSerializer,
    )

class PostCreateAPIView(CreateAPIView):
    queryset = Post.published.all()
    serializer_class = PostCreateUpdateSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

post_create_api_view = PostCreateAPIView().as_view()


class PostDetailAPIView(RetrieveAPIView):
    queryset = Post.published.all()
    serializer_class = PostDetailSerializer

post_detail_api_view = PostDetailAPIView().as_view()


class PostUpdateAPIView(RetrieveUpdateAPIView()):
    queryset = Post.published.all()
    serializer_class = PostCreateUpdateSerializer

    def perform_update(self, serializer):
        serializer.save(author=self.request.user)

post_update_api_view = PostUpdateAPIView().as_view()


class PostDeleteAPIView(DestroyAPIView):
    queryset = Post.published.all()
    serializer_class = PostDetailSerializer

post_delete_api_view = PostDeleteAPIView().as_view()


class PostListAPIView(ListAPIView):
    queryset = Post.published.all()
    serializer_class = PostListSerializer

post_list_api_view = PostListAPIView().as_view()


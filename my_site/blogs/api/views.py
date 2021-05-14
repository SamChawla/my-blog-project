from blogs.models import Post
from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    RetrieveUpdateAPIView,
    CreateAPIView
)

from .serializers import (
    PostListSerializer, 
    PostCreateUpdateSerializer,
)

from rest_framework.permissions import IsAuthenticated
from .permissions import IsPostAuthor


class PostListAPIView(ListAPIView):
    queryset = Post.published.all()
    serializer_class = PostListSerializer

post_list_api_view = PostListAPIView().as_view()


class PostDetailAPIView(RetrieveAPIView):
    queryset = Post.published.all()
    serializer_class = PostListSerializer

post_detail_api_view = PostDetailAPIView().as_view()


class PostCreateAPIView(CreateAPIView):
    queryset = Post.published.all()
    serializer_class = PostCreateUpdateSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

post_create_api_view = PostCreateAPIView().as_view()


class PostUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Post.published.all()
    serializer_class = PostCreateUpdateSerializer
    permission_classes = [IsAuthenticated, IsPostAuthor]

post_update_api_view = PostUpdateAPIView().as_view()
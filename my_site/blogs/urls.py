from django.urls import path
from . import views
# from .views import BlogCreateView

urlpatterns = [
    # path("", views.home, name="blog-home"),
    path("", views.post_list_view, name="blog-home"),
    path('posts/<int:pk>/', views.post_detail_view, name='post-detail'),
    path("posts/new/", views.post_create_view, name="post-create"),
    path('posts/<int:pk>/update/', views.post_update_view, name='post-update'),
    path('posts/<int:pk>/delete/', views.post_delete_view, name='post-delete'),
    path("about/", views.about, name="blog-about"),
    # path('blog/new/', BlogCreateView.as_view(), name='blog-create'),
    
]

from django.urls import path
from . import views

urlpatterns = [
    path("", views.post_list_view, name="blog-home"),
    path('posts/<int:pk>/', views.post_detail_view, name='post-detail'),
    path("posts/new/", views.post_create_view, name="post-create"),
    path('posts/<int:pk>/update/', views.post_update_view, name='post-update'),
    path('posts/<int:pk>/delete/', views.post_delete_view, name='post-delete'),
    path("about/", views.about, name="blog-about"),
]

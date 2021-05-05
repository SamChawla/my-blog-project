from django.urls import path
from . import views

urlpatterns = [
    # path("", views.home, name="blog-home"),
    path("posts/", views.post_list_view, name="blog-home"),
    path('posts/<int:pk>/', views.post_detail_view, name='post-detail'),
    path("about/", views.about, name="blog-about"),
]

from django.urls import path
from . import views

urlpatterns = [
    path("", views.post_list_api_view, name="post-list-api"),
    path('<int:pk>/', views.post_detail_api_view, name='post-detail-api'),
    path("posts/create/", views.post_create_api_view, name="post-create-api"),
    path('<int:pk>/update/', views.post_update_api_view, name='post-update-api'),
    path('<int:pk>/delete/', views.post_delete_api_view, name='post-delete-api'),
    # path("about/", views.about, name="blog-about"),
]

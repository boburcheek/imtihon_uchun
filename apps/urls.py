from django.urls import path
from .views import PostListAPIView, PostRetrieveAPIView


urlpatterns = [
    path("posts/", PostListAPIView.as_view(), name='posts'),
    path("posts/<int:pk>", PostRetrieveAPIView.as_view(), name='post_detail')

]



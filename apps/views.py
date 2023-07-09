from django.shortcuts import render
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateAPIView
from .models import Post
from .permissions import IsOwnerOrReadOnly
from .serializers import PostSerializer
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly


class PostListAPIView(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )

    def perform_create(self, serializers):
        serializers.save(owner=self.request.user)


class PostRetrieveAPIView(RetrieveUpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsOwnerOrReadOnly,)

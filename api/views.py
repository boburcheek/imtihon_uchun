from rest_framework.generics import ListAPIView, UpdateAPIView, CreateAPIView, RetrieveAPIView
from .serializer import AuthorSerializer, BookSerializer
from . import serializer
from .models import Book, Author


class BookListApiView(ListAPIView):
    serializer_class = serializer.BookSerializer
    queryset = Book.objects.all().order_by("-id")


class BookUpdateApiView(UpdateAPIView):
    serializer_class = serializer.BookSerializer
    model = Book


class BookCreatedApiView(CreateAPIView):
    serializer_class = serializer.BookSerializer
    model = Book


class AuthorApiView(ListAPIView):
    serializer_class = serializer.AuthorSerializer
    queryset = Author.objects.all().order_by("-id")


class AuthorRetrieveAPIView(RetrieveAPIView):
    queryset = Author.objects.all().order_by("-id")
    serializer_class = serializer.AuthorSerializer


class BookRetrieveAPIView(RetrieveAPIView):
    queryset = Book.objects.all().order_by("-id")
    serializer_class = serializer.BookSerializer


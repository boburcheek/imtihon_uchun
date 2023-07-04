from rest_framework.generics import ListAPIView, UpdateAPIView, CreateAPIView, ListCreateAPIView, RetrieveAPIView
from .serializer import AuthorSerializer, BookSerializer
from . import serializer
from .models import Book, Author


class BookListApiView(ListAPIView):
    serializer_class = serializer.BookSerializer
    queryset = Book.objects.all()


class AuthorApiView(ListAPIView):
    serializer_class = serializer.AuthorSerializer
    queryset = Author.objects.all()


class AuthorRetrieveAPIView(RetrieveAPIView):
    queryset = Author.objects.all().order_by()
    serializer_class = serializer.AuthorSerializer


class BookRetrieveAPIView(RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = serializer.BookSerializer

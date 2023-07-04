from rest_framework.serializers import ModelSerializer
from .models import Book, Author
from . import models


class AuthorSerializer(ModelSerializer):

    class Meta:
        model = models.Author
        fields = ("id","full_name", "photo", "created_at")


class BookSerializer(ModelSerializer):
    class Meta:
        model = models.Book
        fields = ("id", "title")


from django.contrib import admin
from . import models


@admin.register(models.Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ("id", "full_name")
    list_filter = ("created_at", "update_at")


@admin.register(models.Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("id", "description", "title")
    list_filter = ("created_at", "update_at")
    search_fields = ("title",)

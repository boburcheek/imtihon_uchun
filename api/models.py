from django.db import models


class BaseModel(models.Model):
    created_at = models.DateField(auto_now_add=True)
    update_at = models.DateField(auto_now=True)

    class Meta:
        abstract = True


class Author(BaseModel):
    full_name = models.CharField(max_length=100)
    website = models.URLField()
    photo = models.ImageField(upload_to="author/", verbose_name="Image")
    about = models.TextField()

    def __str__(self):
        return self.full_name


class Book(BaseModel):
    title = models.CharField(max_length=200)
    description = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.title}{self.author}"

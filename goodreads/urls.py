
from django.contrib import admin
from django.urls import path
from api.views import AuthorApiView, BookListApiView, AuthorRetrieveAPIView, BookRetrieveAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('book/', BookListApiView.as_view()),
    path('author/', AuthorApiView.as_view()),
    path("authors/<int:pk>", AuthorRetrieveAPIView.as_view()),
    path("books/<int:pk>", BookRetrieveAPIView.as_view())

]

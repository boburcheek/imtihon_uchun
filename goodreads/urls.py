
from django.contrib import admin
from django.urls import path, include
from api.views import AuthorApiView, BookListApiView, AuthorRetrieveAPIView, BookRetrieveAPIView, BookUpdateApiView, BookCreatedApiView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('book/', BookListApiView.as_view()),
    path('author/', AuthorApiView.as_view()),
    path("authors/<int:pk>", AuthorRetrieveAPIView.as_view()),
    path("books/<int:pk>", BookRetrieveAPIView.as_view()),
    path('books/create/', BookCreatedApiView.as_view()),
    path('books/<int:pk>/update/', BookUpdateApiView.as_view()),
    path('apps/', include("apps.urls")),
    path("api/v1/apps", include("users.urls"))


]

urlpatterns += [
    path('api-auth/', include('rest_framework.urls'))
]

from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import AllowAny
from rest_framework import filters
from .serializers import AuthorSerializer
from .models import Author

from .models import Book, Category, SubCategory, FeedBack
from .serializers import (
    BookSerializer,
    CategorySerializer,
    FeedBackSerializer
)


class ListRetrieveBook(ReadOnlyModelViewSet):
    """
    Получение всех книг, книг по категории, поиск и конкретной книги.
    """

    queryset = Book.objects.all().order_by('-publisheddate')
    serializer_class = BookSerializer

    filter_backends = (DjangoFilterBackend, filters.SearchFilter)

    filterset_fields = (
        'categories',
        'categories__title',
        'title',
        'authors',
        'status',
        'publisheddate',
    )

    search_fields = (
        'title',
    )

    permission_classes = [AllowAny]

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.is_detail_request = True
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class ListCategory(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [AllowAny]
    filter_backends = (filters.SearchFilter,)
    search_fields = ('title',)


class ListSubCategory(ListAPIView):
    queryset = SubCategory.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [AllowAny]


class CreateFeedback(CreateAPIView):
    queryset = FeedBack.objects.all()
    serializer_class = FeedBackSerializer
    permission_classes = [AllowAny]


class ListAuthors(ListAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [AllowAny]
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)
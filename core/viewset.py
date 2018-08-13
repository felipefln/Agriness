from django_filters import rest_framework as filters
from rest_framework import viewsets

from core.models import Article, Author, Category
from core.serializer import (
    ArticleSerializer, ArticleReadSerializer,
    AuthorSerializer, CategorySerializer
)


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = '__all__'


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = '__all__'


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all().order_by('publish_date')
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = '__all__'    

    def get_serializer_class(self):
        if self.request.method in ['GET']:
            return ArticleReadSerializer
        return ArticleSerializer

    def get_queryset(self):
        queryset = queryset = self.queryset
        search = self.request.query_params.get('search')
        if search:
            queryset = queryset.filter(content__icontains=search)
        return queryset
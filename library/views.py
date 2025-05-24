from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated
from .models import Book
from .serializers import BookSerializer
from .permision import IsOwnerOrSuperUser
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi



class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    # filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    # search_fields = ['title', 'author', 'genre']
    # ordering_fields = ['published_year', 'title']
    permission_classes = [IsAuthenticated, IsOwnerOrSuperUser]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @swagger_auto_schema(manual_parameters=[
        openapi.Parameter('name', openapi.IN_QUERY,
                          description="Search by name", type=openapi.TYPE_STRING),
        openapi.Parameter('author', openapi.IN_QUERY,
                          description="Search by author", type=openapi.TYPE_STRING),
    ])

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def get_queryset(self):
        queryset = Book.objects.all()
        if 'name' in self.request.GET:
            queryset = queryset.filter(
                title__icontains=self.request.GET['name'])

        if 'author' in self.request.GET:
            queryset = queryset.filter(
                author__icontains=self.request.GET['author'])
        return queryset

from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated
from .models import Book
from .serializers import BookSerializer 
from .permision import IsOwnerOrSuperUser

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'author', 'genre']
    ordering_fields = ['published_year', 'title']
    permission_classes = [IsAuthenticated, IsOwnerOrSuperUser]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user) 

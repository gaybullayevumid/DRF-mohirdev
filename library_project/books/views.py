from .models import Books
from .serializers import BookSerializer
from rest_framework import generics

# Create your views here.

class BookListApiView(generics.ListAPIView):
    queryset = Books.objects.all()
    serializer_class = BookSerializer
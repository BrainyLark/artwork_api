from rest_framework import permissions, viewsets

from .models import Artist, Product
from .serializers import ArtistSerializer, ProductSerializer, ArtistSimpleSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
class ArtistViewSet(viewsets.ModelViewSet):
    queryset = Artist.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    def get_serializer_class(self):
        if self.action == 'retrieve': # for /artists/<pk>/
            return ArtistSerializer
        
        return ArtistSimpleSerializer
    
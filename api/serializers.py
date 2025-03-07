from rest_framework import serializers
from .models import Artist, Product

class ProductSimpleSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Product
        fields = ['id', 'title', 'image', 'price']

class ArtistSimpleSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Artist
        fields = ['id', 'name', 'profile']

class ProductSerializer(serializers.ModelSerializer):
    
    artist = ArtistSimpleSerializer(many=False, read_only=True)
    
    class Meta:
        model = Product
        fields = [
            'id',
            'title',
            'description',
            'image',
            'artist',
            'price',
            'width',
            'height',
            'category',
            'technique',
            'created_at',
        ]


class ArtistSerializer(serializers.ModelSerializer):
    
    products = ProductSimpleSerializer(many=True, read_only=True)
    
    class Meta:
        model = Artist
        fields = [
            'id',
            'name',
            'description',
            'profile',
            'contact',
            'products',
            'created_at',
        ]
        
from django.contrib import admin
from .models import Product, Artist

# Register your models here.
admin.site.register(Artist)
admin.site.register(Product)
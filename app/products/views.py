from rest_framework import generics

from .models import ProductModel
from .serializer import ProductSerializer

class ProductsList(generics.ListCreateAPIView):
    queryset = ProductModel.objects.all()
    serializer_class = ProductSerializer

class CreateProduct(generics.CreateAPIView):
    queryset = ProductModel.objects.all()
    serializer_class = ProductSerializer

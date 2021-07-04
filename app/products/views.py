from django.http.response import Http404
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import ProductModel
from .serializer import ProductSerializer

class AllProducts(APIView):

    def get(self, request):

        products = ProductModel.objects.all()
        product_serializer = ProductSerializer(products, many=True)
        return Response(product_serializer.data)

    def post(self, request):

        data = {

            'name_product': request.data.get('name_product'),
            'plataform': request.data.get('plataform'),
            'price': request.data.get('price'),
            'restaurant': request.data.get('restaurant'),
            'category': request.data.get('category')

        }

        product_serializer = ProductSerializer(data=data)

        if product_serializer.is_valid():
            product_serializer.save()
            return Response(product_serializer.data)
        else:
            return Response(product_serializer.errors)

class AllCategorys(APIView):
    
    def get(self, request):

        product_category = self.get_category(pk)
        serializer = ProductSerializer(product_category)
        return Response(serializer.data)
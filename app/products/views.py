from django.http.response import Http404
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import ProductModel
from .serializer import ProductSerializer


class AllProducts(APIView):

    def get(self, request, format=None):

        products = ProductModel.objects.all()
        product_serializer = ProductSerializer(products,many=True)
        return Response(product_serializer.data)

class AllCategorys(APIView):

    def get(sel, request, format=None):

        products_categorys = [category.category for category in ProductModel.objects.all()]
        return Response(products_categorys)

class AddProduct(APIView):


    def post(self, request):


        data = {

            'name_product': request.data.get('name_product'),
            'plataform': request.data.get('plataform'),
            'price': request.data.get('price'),
            'restaurant': request.data.get('restaurant'),
            'category': request.data.get('category'),

        }

        products = ProductSerializer(data=data)

        if products.is_valid():
            products.save()
            return Response(products.data)
        else:
            return Response(products.errors)


class ProductById(APIView):

    def get_product(self, id):
        try:
            return ProductModel.objects.get(id=id)
        except ProductModel.DoesNotExist:
            return Http404

    def get(self, request, id,format=None):

        product = self.get_product(id=id)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

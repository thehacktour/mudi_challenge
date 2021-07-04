from rest_framework.views import APIView
from rest_framework.response import Response

from .models import ProductModel
from .serializer import ProductSerializer

class AllCategorys(APIView):

    def get(sel, request, format=None):

        products_categorys = [category.category for category in ProductModel.objects.all()]
        return Response(products_categorys)

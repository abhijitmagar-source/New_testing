from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Product,Inventory
from .serializers import ProductSerializers
from rest_framework.views import APIView
from rest_framework import status

class ProductCreateView(APIView):

    def post(self,request):
        serializer = ProductSerializers(data=request.data)

        if serializer.is_valid():
           serializer.save()
           return Response({"message":"Product added sucesfully"},status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
class FetchProducts(APIView):

    def get(self,request):
        products = Product.objects.all()
        serializer = ProductSerializers(products,many=True)

        return Response(serializer.data,status=status.HTTP_200_OK)
    

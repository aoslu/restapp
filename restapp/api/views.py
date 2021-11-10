from rest_framework import status
from rest_framework.response import Response
from restapp.models import Customers, ProductModel, KategoriModel,Makale, Gazeteci
from restapp.api.serializers import CustomersSerializer, ProductModelSerializer, KategoriModelSerializer,MakaleSerializer,GazeteciSerializer
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404


class CustomerListCreateAPIView(APIView):
    def get(self, request):
        customers= Customers.objects.filter()
        serializer = CustomersSerializer(customers, many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer =CustomersSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        return Response(status= status.HTTP_400_BAD_REQUEST)


#FUNCTİON BASED VİEWS
# @api_view(['GET', 'POST'])
# def customer_list_create_api_view(request):
#     if request.method == 'GET':
#         customers= Customers.objects.filter()
#         serializer = CustomersSerializer(customers, many=True)
#         return Response(serializer.data)
#     elif request.method== 'POST':
#         serializer =CustomersSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status= status.HTTP_201_CREATED)
#         return Response(status= status.HTTP_400_BAD_REQUEST)

class CustomerDetailAPIView(APIView):
    def get_object(self, pk):
        xd= get_object_or_404(Customers, pk=pk)
        return xd

    def get(self, request, pk):
        customer = self.get_object(pk=pk)
        serializer = CustomersSerializer(customer)
        return Response(serializer.data)

    def put(self, request,pk):
        customer= self.get_object(pk=pk)
        serializer =CustomersSerializer(customer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        customer = self.get_object(pk=pk)
        customer.delete()
        return Response(status= status.HTTP_204_NO_CONTENT)

class ProductModelListCreateAPIView(APIView):
    def get(self, request):
        products= ProductModel.objects.filter()
        serializer = ProductModelSerializer(products, many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer =ProductModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        return Response(status= status.HTTP_400_BAD_REQUEST)

class ProductModelDetailAPIView(APIView):
    def get_object(self, pk):
         products= get_object_or_404(ProductModel, pk=pk)
         return products

    def get(self, request, pk):
        products = self.get_object(pk=pk)
        serializer = ProductModelSerializer(products)
        return Response(serializer.data)

    def put(self, request,pk):
        products= self.get_object(pk=pk)
        serializer =ProductModelSerializer(products, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        product = self.get_object(pk=pk)
        product.delete()
        return Response(status= status.HTTP_204_NO_CONTENT)


class KategoriModelListCreateAPIView(APIView):
    def get(self, request):
        kategori= KategoriModel.objects.filter()
        serializer = KategoriModelSerializer(kategori, many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer =KategoriModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        return Response(status= status.HTTP_400_BAD_REQUEST)

class KategoriModelDetailAPIView(APIView):
    def get_object(self, pk):
         products= get_object_or_404(KategoriModel, pk=pk)
         return products

    def get(self, request, pk):
        kategori = self.get_object(pk=pk)
        serializer = KategoriModelSerializer(kategori)
        return Response(serializer.data)

    def put(self, request,pk):
        kategori= self.get_object(pk=pk)
        serializer =KategoriModelSerializer(kategori, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        kategori = self.get_object(pk=pk)
        kategori.delete()
        return Response(status= status.HTTP_204_NO_CONTENT)





class MakaleListCreateAPIView(APIView):
    def get(self, request):
        makale= Makale.objects.filter()
        serializer = MakaleSerializer(makale, many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer =MakaleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        return Response(status= status.HTTP_400_BAD_REQUEST)

class MakaleDetailAPIView(APIView):
    def get_object(self, pk):
         makale= get_object_or_404(Makale, pk=pk)
         return makale

    def get(self, request, pk):
        makale = self.get_object(pk=pk)
        serializer = MakaleSerializer(makale)
        return Response(serializer.data)

    def put(self, request,pk):
        makale= self.get_object(pk=pk)
        serializer =MakaleSerializer(makale, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        makale = self.get_object(pk=pk)
        makale.delete()
        return Response(status= status.HTTP_204_NO_CONTENT)

#FUNCTİON BASED VİEWS

# @api_view(['GET','PUT','DELETE'])
# def customer_detail_api_view(request,pk):
#     try:
#         customer_instance= Customers.objects.get(pk=pk)
#     except Customers.DoesNotExist:
#         return Response(
#             {
#             'errors': {
#                 'code': 404,
#                 'message': f'Böyle bir id {{pk}} ile ilgili müşteri yorumu bulunmadı'
#             }
#         },
#         status=status.HTTP_404_NOT_FOUND
#     )
#     if request.method=='GET':
#         serializer = CustomersSerializer(customer_instance)
#         return Response(serializer.data)
#     elif request.method=='PUT':
#         serializer =CustomersSerializer(customer_instance, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(status= status.HTTP_400_BAD_REQUEST)
#     elif request.method=='DELETE':
#         customer_instance.delete()
#         return Response(
#             {
#             'errors': {
#                 'code':204,
#                 'message': f'{{pk}} id numaralı makale silimiştir'
#             }
#         },
#             status= status.HTTP_204_NO_CONTENT
#         )

#@api_view(['GET', 'POST'])
#def urun_list_create_api_view(request):

#    if request.method == 'GET':
#        urunlerim = ProductModel.objects.filter() #Nesnelerden oluşan bir sorgu kümesi
#        serializer = ProductModelSerializer(urunlerim, many=True)
#        return Response(serializer.data)
#    elif request.method== 'POST':
#        serializer = ProductModelSerializer(data=request.data)
#        if serializer.is_valid():
#            serializer.save()
#            return Response(serializer.data, status = status.HTTP_201_CREATED)
#        return Response(status = status.HTTP_400_BAD_REQUEST)
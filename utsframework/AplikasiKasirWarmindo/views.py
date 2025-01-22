from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.hashers import make_password
from .models import User, Barang, Penjualan
from .serializers import BarangSerializer, PenjualanSerializer, TokenCreate, UserSerializer


class TokenCreateView(TokenObtainPairView):
    serializer_class = TokenCreate
    
class UserView(APIView):
    authentication_classes = [TokenAuthentication]

    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.validated_data['password'] = make_password(serializer.validated_data['password'])
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def put(self, request, pk):
        user = User.objects.get(pk=pk)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        user = User.objects.get(pk=pk)
        user.delete()
        return Response(status=204)

class BarangView(APIView):
    authentication_classes = [TokenAuthentication]

    def get(self, request):
        barang = Barang.objects.all()
        serializer = BarangSerializer(barang, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BarangSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def put(self, request, pk):
        barang = Barang.objects.get(pk=pk)
        serializer = BarangSerializer(barang, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        barang = Barang.objects.get(pk=pk)
        barang.delete()
        return Response(status=204)

class PenjualanView(APIView):
    authentication_classes = [TokenAuthentication]

    def get(self, request):
        penjualan = Penjualan.objects.all()
        serializer = PenjualanSerializer(penjualan, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PenjualanSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def put(self, request, pk):
        penjualan = Penjualan.objects.get(pk=pk)
        serializer = PenjualanSerializer(penjualan, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        penjualan = Penjualan.objects.get(pk=pk)
        penjualan.delete()
        return Response(status=204)

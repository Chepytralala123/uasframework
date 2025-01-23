from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import User, Barang, Penjualan

# Custom TokenObtainPairSerializer
class TokenCreate(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username
        token['isadmin'] = user.isadmin
        token['ismanager'] = user.ismanager
        token['iskasir'] = user.iskasir

        return token

# Serializer for User model
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'nama_lengkap', 'email', 'isadmin', 'ismanager', 'iskasir']

# Serializer for Barang model
class BarangSerializer(serializers.ModelSerializer):
    class Meta:
        model = Barang
        fields = ['id', 'nama_produk', 'harga', 'deskripsi', 'stok']

# Serializer for Penjualan model
class PenjualanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Penjualan
        fields = ['user', 'barang', 'tanggal_penjualan', 'total_harga']

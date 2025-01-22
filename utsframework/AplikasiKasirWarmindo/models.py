from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.db import models
# from django.utils.translation import gettext_lazy as _

class User(AbstractUser, PermissionsMixin):
    username = models.CharField(max_length=50, unique=True)
    nama_lengkap = models.CharField(max_length=100)
    email = models.EmailField(blank=True)
    isadmin = models.BooleanField(default=False)
    ismanager = models.BooleanField(default=False)
    iskasir = models.BooleanField(default=False)


class Barang(models.Model):
    nama_produk = models.CharField(max_length=100)
    harga = models.DecimalField(max_digits=10, decimal_places=2)
    deskripsi = models.TextField()
    stok = models.PositiveIntegerField()


class Penjualan(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    barang = models.ForeignKey(Barang, on_delete=models.SET_NULL, null=True)
    tanggal_penjualan = models.DateTimeField(auto_now_add=True)
    total_harga = models.DecimalField(max_digits=10, decimal_places=2)
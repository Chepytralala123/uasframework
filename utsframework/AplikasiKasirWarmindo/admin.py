from django.contrib import admin
from .models import User, Barang, Penjualan

# Register your models here.
admin.site.register(User)
admin.site.register(Barang)
admin.site.register(Penjualan)

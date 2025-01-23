from django.urls import path
from .views import UserView, BarangView, PenjualanView, TokenCreateView

urlpatterns = [
    path('users/', UserView.as_view(), name='users-list'),
    path('users/<int:pk>/', UserView.as_view(), name='users-detail'),
    path('barang/', BarangView.as_view(), name='barang-list'),
    path('barang/<uuid:pk>/', BarangView.as_view(), name='barang-detail'),
    path('penjualan/', PenjualanView.as_view(), name='penjualan-list'),
    path('penjualan/<int:pk>/', PenjualanView.as_view(), name='penjualan-detail'),
    path('login/', TokenCreateView.as_view(), name='login'),
]

from django.contrib import admin
from django.urls import path,include
from .views import *
urlpatterns = [
    path('create_product/',ProductCreateView.as_view(),name='create_product'),
    path('update_product/<int:pk>',ProductUpdateView.as_view(),name='update_product'),
    path('delete_product/<int:pk>',ProductDeleteView.as_view(),name='delete_product'),
    path('product_list/',ProductListView.as_view(),name='product_list'),
    path('product_detail/<int:pk>',ProductDetailView.as_view(),name='product_detail'),
    path('cart/addtocart/<int:pk>', AddToCartView.as_view(), name='addtocart'),
    path('cart/removefromcart/<int:pk>', RemoveFromCartView.as_view(), name='removefromcart'),
    path('cart/', CartView.as_view(), name='cart'),
]

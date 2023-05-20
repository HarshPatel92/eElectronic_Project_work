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
    path('order/', OrderView.as_view(),name='order'),
    #path('checkoutsuccess/',Checkout_success_view.as_view(),name='checkoutsuccess').
    path('checkoutsuccess/',TemplateView.as_view(template_name='product/checkout_success.html'),name='checkoutsuccess'),
    
    path('create-order/', OrderCreateView.as_view(), name='order_create'),
    path('order-list/', OrderListView.as_view(), name='order_list'),
    
]

from django.contrib import admin
from django.urls import path,include
from .views import UserRegisterView,VendorRegisterView,AdminRegisterView,UserLoginView,VendorDashboardView

urlpatterns = [
    path('userregister/',UserRegisterView.as_view(),name='userregister'),
    path('vendorregister/',VendorRegisterView.as_view(),name='vendorregister'),
    path('adminregister/',AdminRegisterView.as_view(),name='adminregister'),
    path('login/',UserLoginView.as_view(),name='login'),
    #path('logout/',UserLogoutView.as_view(),name='logout'),
    path('vendor/dashboard/',VendorDashboardView.as_view(),name='vendor_dashboard'),
    
]

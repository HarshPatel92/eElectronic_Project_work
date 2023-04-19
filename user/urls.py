from django.contrib import admin
from django.urls import path,include
from .views import *

urlpatterns = [
    path('userregister/',UserRegisterView.as_view(),name='userregister'),
    path('vendorregister/',VendorRegisterView.as_view(),name='vendorregister'),
    path('adminregister/',AdminRegisterView.as_view(),name='adminregister'),
    path('login/',UserLoginView.as_view(),name='login'),
    path('logout/',UserLogoutView.as_view(),name='logout'),
    path('vendor/dashboard/',VendorDashboardView.as_view(),name='vendor_dashboard'),
    path('admin/dashboard/',AdminDashboardView.as_view(),name='admin_dashboard'),
    path('user/dashboard/',UserDashboardView.as_view(),name='user_dashboard'),
    path('userprofile/',UserProfileView.as_view(),name='userprofile'),
    path('register/',TemplateView.as_view(template_name='product/register.html'),name='register'),
    path('about/',TemplateView.as_view(template_name='about.html'),name='about')
]

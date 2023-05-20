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
    path('profile/', UserProfileView.as_view(), name='user_profile'),
    path('profile/update/<int:pk>', UserProfileUpdateView.as_view(), name='user_profile_update'),
    path('register/',TemplateView.as_view(template_name='product/register.html'),name='register'),
    path('aboutus/',TemplateView.as_view(template_name='user/aboutus.html'),name='aboutus'),
    path('contactus/',ContactView.as_view(),name='contactus'),
    path('contactus/success/',TemplateView.as_view(template_name='user/contact_success.html'),name='contactsuccess')
]

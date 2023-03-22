from django.shortcuts import render,redirect
from django.views.generic.edit import CreateView
from .models import User
from .forms import UserRegisterForm,VendorRegisterForm,AdminRegisterForm
from django.contrib.auth import login
from django.contrib.auth.views import LoginView,LogoutView
from django.views.generic import ListView
from product.models import Product

class UserRegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'user/user_register.html'
    success_url = '/user/login/'
    
    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'user'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        #email = form.cleaned_data.get('email')
        user = form.save()
        login(self.request,user)
        return super().form_valid(form)
    
class VendorRegisterView(CreateView):
    model = User
    form_class = VendorRegisterForm
    template_name = 'user/vendor_register.html'
    success_url = '/user/login/'
    
    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'vendor'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        #email = form.cleaned_data.get('email')
        user = form.save()
        login(self.request,user)
        return super().form_valid(form)
    
class AdminRegisterView(CreateView):
    model = User
    form_class = AdminRegisterForm
    template_name = 'user/admin_register.html'
    success_url = '/user/login/'
    
    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'admin'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        #email = form.cleaned_data.get('email')
        user = form.save()
        login(self.request,user)
        return super().form_valid(form)
    
class UserLoginView(LoginView):
    template_name = 'user/login.html'
    #success_url = '/user/login/'
    
    def get_redirect_url(self):
        if self.request.user.is_authenticated:
           if self.request.user.is_user:
            return '/user/user_dashboard'
           elif self.request.user.is_vendor:
            return '/user/vendor/dashboard'
           else:
            return '/user/admin_dashboard'
        
class VendorDashboardView(ListView):
    def get(self, request, *args, **kwargs):
        product = Product.objects.all().values()
        
        return render(request, 'user/vendor_dashboard.html',{
            'products':product,
        })

    template_name = 'user/vendor_dashboard.html'

            
    
    
    
        
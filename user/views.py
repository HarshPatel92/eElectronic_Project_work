from django.shortcuts import render,redirect
from django.views.generic.edit import CreateView
from .models import User
from .forms import UserRegisterForm,VendorRegisterForm,AdminRegisterForm
from django.contrib.auth import login
from django.contrib.auth.views import LoginView,LogoutView
from django.views.generic import ListView
from product.models import Product
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .decorators import user_required,vendor_required,admin_required

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
            return '/user/user/dashboard'
           elif self.request.user.is_vendor:
            return '/user/vendor/dashboard'
           else:
            return '/user/admin/dashboard'

@method_decorator([login_required(login_url='/user/login/'),vendor_required],name='dispatch')       
class VendorDashboardView(ListView):
    def get(self, request, *args, **kwargs):
        product = Product.objects.all().values()
        
        return render(request, 'user/vendor_dashboard.html',{
            'products':product,
        })

    template_name = 'user/vendor_dashboard.html'

@method_decorator([login_required(login_url='/user/login/'),admin_required],name='dispatch')
class AdminDashboardView(ListView):

    template_name = 'user/admin_dashboard.html'
    
@method_decorator([login_required(login_url='/user/login/'),user_required],name='dispatch')
class UserDashboardView(ListView):
    template_name = 'user/user_dashboard.html'
    context_object_name = 'user_dashboard'
    
    
    
    
       
    
    
    
        
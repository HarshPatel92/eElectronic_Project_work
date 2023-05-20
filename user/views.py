from django.shortcuts import render,redirect
from django.views.generic.edit import CreateView,UpdateView
from .models import User
from .forms import UserRegisterForm,VendorRegisterForm,AdminRegisterForm,UserProfileForm,ContactForm
from django.contrib.auth import login
from django.contrib.auth.views import LoginView,LogoutView
from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic import ListView,TemplateView,FormView,DetailView
from product.models import Product
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .decorators import user_required,vendor_required,admin_required
from django.core.mail import send_mail
from django.conf import settings


class IndexView(TemplateView):
    template_name = 'user/index.html'
class UserRegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'user/user_register.html'
    success_url = '/user/login/'
    
    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'user'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        email = form.cleaned_data.get('email')
        user = form.save()
        recipient_list = [email]
        subject = "welcome to E-electronics Website"
        message = "Say hello to Django!! You are User now !! Now you can purchase electronics items from website according to your requirement."
        email_from = settings.EMAIL_HOST_USER
        send_mail(subject, message, email_from, recipient_list)
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
        email = form.cleaned_data.get('email')
        user = form.save()
        recipient_list = [email]
        subject = "welcome to E-electronics Website"
        message = "Say hello to Django!! You are Vendor now"
        email_from = settings.EMAIL_HOST_USER
        send_mail(subject, message, email_from, recipient_list)
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
        email = form.cleaned_data.get('email')
        user = form.save()
        recipient_list = [email]
        subject = "welcome to E-electronics Website"
        message = "Say hello to Django!! You are Admin now"
        email_from = settings.EMAIL_HOST_USER
        send_mail(subject, message, email_from, recipient_list)
        login(self.request,user)
        return super().form_valid(form)
    
class UserLoginView(LoginView):
    template_name = 'user/login.html'
    success_url = '/user/login/'
    
    def get_redirect_url(self):
        if self.request.user.is_authenticated:
           if self.request.user.is_user:
            return '/user/user/dashboard'
           elif self.request.user.is_vendor:
            return '/user/vendor/dashboard'
           else:
            return '/user/admin/dashboard'
        
class UserLogoutView(LogoutView):
    next_page = reverse_lazy('login')
    
    # def dispatch(self, request, *args, **kwargs):
    #     response = super().dispatch(request, *args, **kwargs)
    #     messages.success(request, "You have been logged out.")
    #     return response


@method_decorator([login_required(login_url='/user/login/'),vendor_required],name='dispatch')       
class VendorDashboardView(ListView):
    def get(self, request, *args, **kwargs):
        product = Product.objects.filter()
        sort_by = self.request.GET.get('sort_by','product_name')
        direction = self.request.GET.get('direction','asc')
        print(".....",sort_by)
        print(".....",direction)
        if direction == 'asc':
            product = product.order_by(sort_by)
        elif direction == 'desc':
            product = product.order_by(f'-{sort_by}')
        
        return render(request, 'user/vendor_dashboard.html',{
            'products':product,
        })

    template_name = 'user/vendor_dashboard.html'

@method_decorator([login_required(login_url='/user/login/'),admin_required],name='dispatch')
class AdminDashboardView(TemplateView):

    template_name = 'user/admin_dashboard.html'
    
@method_decorator([login_required(login_url='/user/login/'),user_required],name='dispatch')
class UserDashboardView(TemplateView):
    template_name = 'user/user_dashboard.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #user = self.request.user
        products = Product.objects.filter()
        context['products'] = products
        return context
    

class UserProfileView(CreateView):
    model = User
    form_class = UserProfileForm
    template_name = 'user/user_profile.html'
    
    def get_initial(self):
        initial = super().get_initial()
        initial.update({
            'first_name': self.request.user.first_name,
            'last_name': self.request.user.last_name,
            'email': self.request.user.email,
            'age': self.request.user.age,
            'profile_pic': self.request.user.profile_pic,
        })
        return initial
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
    def get_redirect_url(self):
      if self.request.user.is_authenticated:
        if self.request.user.is_user:
            return 'user/user/dashboard/'
        elif self.request.user.is_vendor:
            return 'user/vendor/dashboard/'
        else:
            return 'user/admin/dashboard/'
        
class UserProfileUpdateView(UpdateView):
    model = User
    form_class = UserProfileForm
    template_name = 'user/user_profile_update.html'
    success_url = reverse_lazy('user_profile')

    def get_object(self):
        return self.request.user

    def get_success_url(self):
        return reverse_lazy('user_profile', kwargs={'pk': self.object.pk})

    
class ContactView(FormView):
    template_name = 'user/contactus.html'
    form_class = ContactForm
    success_url = reverse_lazy('contactsuccess')

    def form_valid(self, form):
        name = form.cleaned_data.get('name', '')
        email = form.cleaned_data.get('email', '')
        message = form.cleaned_data.get('message', '')

        # Send email to site owner
        send_mail(
            'New message from Contact Us form',
            f'Name: {name}\nEmail: {email}\nMessage: {message}',
            email, # From email address
            [settings.EMAIL_HOST_USER], # To email address
            fail_silently=False,
        )

        return super().form_valid(form) 

    
    
       
    
    
    
        
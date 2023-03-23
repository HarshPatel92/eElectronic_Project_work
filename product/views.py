from django.shortcuts import render
from django.views.generic import CreateView,UpdateView,DeleteView,ListView,DetailView
from .forms import *
from .models import *
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from user.decorators import user_required,admin_required,vendor_required
# Create your views here.

class ProductCreateView(CreateView):
    form_class = ProductCreationForm
    model = Product
    template_name = 'product/create_product.html'
    success_url = '/product/product_list/'
    
    def form_valid(self, form):
        return super().form_valid(form)
    
class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductCreationForm
    template_name = 'product/create_product.html'
    success_url ='/product/product_list/'
    
class ProductDeleteView(DeleteView):
    model = Product
    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)
        
    success_url = '/product/product_list/'
    
class ProductListView(ListView):
    model = Product
    template_name = 'product/product_list.html'
    context_object_name = 'product_list'
    
    def get_queryset(self):
        return super().get_queryset()
    
class ProductDetailView(DetailView):
    model = Product
    template_name = 'product/product_detail.html'
    context_object_name = 'product_detail'
    
    def get(self, request, *args, **kwargs):
        return render(request,self.template_name)
    
    
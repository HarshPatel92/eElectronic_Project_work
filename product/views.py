from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic import CreateView,UpdateView,DeleteView,ListView,DetailView,TemplateView,FormView,View
from .forms import *
from .models import *
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from user.decorators import user_required,admin_required,vendor_required
from django.contrib import messages
# Create your views here.

class ProductCreateView(CreateView):
    form_class = ProductCreationForm
    model = Product
    template_name = 'product/create_product.html'
    success_url = '/product/product_list/'
    
    def form_valid(self, form):
        response = super().form_valid(form)
        
        if self.request.POST.get('saveAndAddAnother'):
            return redirect('create_product')
        
        return response
        
    
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
    
    def get(self, request, *args, **kwargs):
        product = Product.objects.filter()
        sort_by = self.request.GET.get('sort_by','product_name')
        direction = self.request.GET.get('direction','asc')
        print("sort by ",sort_by)
        print("direction is ",direction)
        if direction == 'asc':
            product = product.order_by(sort_by)
        elif direction == 'desc':
            product = product.order_by(f'-{sort_by}')
        return render(request, self.template_name,{'product_list':product})
class ProductDetailView(DetailView):
    model = Product
    template_name = 'product/product_detail.html'
    context_object_name = 'product_detail'
    
    def get(self, request, *args, **kwargs):
        return render(request,self.template_name,{'product_detail':self.get_object()})


class CartView(ListView):
    model = Cart_detail
    template_name = 'product/cart.html'

    def get_queryset(self):
        user = self.request.user
        try:
            cart = Cart.objects.get(user=user)
        except Cart.DoesNotExist:
            return Cart_detail.objects.none()
        return cart.cart_detail_set.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        try:
            cart = Cart.objects.get(user=user)
        except Cart.DoesNotExist:
            cart = None
        total = 0
        if cart:
            for cart_detail in cart.cart_detail_set.all():
                total += cart_detail.price
        context['total'] = total
        return context
class AddToCartView(View):
    def get(self, request, pk):
        product = Product.objects.get(pk=pk)
        user = request.user
        try:
            cart = Cart.objects.get(user=user)
        except Cart.DoesNotExist:
            cart = Cart.objects.create(user=user)
        try:
            cart_detail = Cart_detail.objects.get(cart=cart, product=product)
            cart_detail.quantity += 1
            cart_detail.price += product.price
            cart_detail.save()
        except Cart_detail.DoesNotExist:
            cart_detail = Cart_detail.objects.create(cart=cart, product=product, quantity=1, price=product.price)
        messages.info(request, product.product_name + ' Added into cart successfully!')
        return redirect('cart')
        


class RemoveFromCartView(View):
    def get(self, request, pk):
        product = Product.objects.get(pk=pk)
        user = request.user
        cart = Cart.objects.get(user=user)
        cart_detail = Cart_detail.objects.get(cart=cart, product=product)
        cart_detail.quantity -= 1
        cart_detail.price -= product.price
        if cart_detail.quantity == 0:
            cart_detail.delete()
        else:
            cart_detail.save()
        messages.info(request, product.product_name + ' removed from cart successfully!')
        return redirect('cart')

    
class OrderView(ListView):
    model = Cart_detail
    template_name = 'product/order.html'

    def get_queryset(self):
        user = self.request.user
        try:
            cart = Cart.objects.get(user=user)
        except Cart.DoesNotExist:
            return Cart_detail.objects.none()
        return cart.cart_detail_set.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        try:
            cart = Cart.objects.get(user=user)
        except Cart.DoesNotExist:
            cart = None
        total = 0
        if cart:
            for cart_detail in cart.cart_detail_set.all():
                total += cart_detail.price
        context['total'] = total
        return context
    
# class Checkout_success_view(TemplateView):
#     template_name= 'product/checkout_success.html'


class OrderCreateView(View):
    def get(self, request):
        user = request.user
        cart = Cart.objects.get(user=user)
        cart_items = cart.cart_detail_set.all()

        if not cart_items:
            messages.error(request, 'Your cart is empty.')
            return redirect('cart')

        address = Customer_address.objects.filter(user=user).first()

        if not address:
            messages.error(request, 'Please add a valid address for delivery.')
            return redirect('cart')

        order = Order.objects.create(user=user, total=0, status=Status.objects.get(status='Available'), address=address)
        total_price = 0

        for item in cart_items:
            Order_detail.objects.create(
                order=order,
                user=user,
                quantity=item.quantity,
                price=item.price,
                product=item.product
            )
            total_price += item.price

        order.total = total_price
        order.save()

        cart_items.delete()
        messages.success(request, 'Order placed successfully. Thank you for your purchase!')
        return redirect('order_list')


class OrderListView(ListView):
    model = Order
    template_name = 'product/order_list.html'
    context_object_name = 'orders'

    def get_queryset(self):
        user = self.request.user
        return Order.objects.filter(user=user)
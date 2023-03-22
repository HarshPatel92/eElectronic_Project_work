from django.db import models
from user.models import User

# from user import User
# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=False)
    
    def __str__(self):
        return self.category_name
    
    class Meta:
        db_table = 'category'
        
class SubCategory(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    subcategory_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.subcategory_name
    
    class Meta:
        db_table = 'subcategory'
        
class Brand(models.Model):
    brand_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.brand_name
    
    class Meta:
        db_table = 'brand'
        
class State(models.Model):
    state_name = models.CharField(max_length=255,unique=True)
    
    def __str__(self):
        return self.state_name
    
    class Meta:
        db_table = 'state'
        
class City(models.Model):
    city_name = models.CharField(max_length=255)
    state = models.ForeignKey(State,on_delete=models.CASCADE)

    def __str__(self):
        return self.city_name
    
    class Meta:
        db_table = 'city'
        
class Vendor_detail(models.Model):
    vendor_name = models.CharField(max_length=255)
    address = models.TextField()
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pincode = models.PositiveIntegerField()
    contact_num = models.CharField(max_length=15)
    customer_support_num = models.CharField(max_length=15)
    feedback_email = models.EmailField()
    
    def __str__(self):
        return self.vendor_name
    
    class Meta:
        db_table = 'vendor_detail'
        
class Customer_address(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    cust_name = models.CharField(max_length=255)
    cust_address = models.TextField()
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    pincode = models.PositiveIntegerField()
    
    def __str__(self):
        return self.cust_name
    
    class Meta:
        db_table = 'cust_address'
        
class Product(models.Model):
    product_name = models.CharField(max_length=255)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    subcategory = models.ForeignKey(SubCategory,on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand,on_delete=models.CASCADE)
    description = models.TextField()
    price = models.FloatField()
    
    def __str__(self):
        return self.product_name
    
    class Meta:
        db_table = 'product'
        
class Vendor_product(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    vendor = models.ForeignKey(Vendor_detail,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.FloatField()
    
    def __str__(self):
        return self.product
    
    class Meta:
        db_table = 'vendor_product'
        
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'cart'
        
class Cart_detail(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    vendorProduct = models.ForeignKey(Vendor_product,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.FloatField()
    
    class Meta:
        db_table = 'cart_detail'
  
  
statusChoice = (("Available","available"),("Not Available","not available"))      
class Status(models.Model):
    status = models.CharField(choices=statusChoice , max_length=255)
    
    class Meta:
        db_table = 'status'

class Order(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)        
    total = models.PositiveIntegerField()
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    address = models.ForeignKey(Customer_address, on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'order'
        
class Order_detail(models.Model):
    order = models.ForeignKey(Order,on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.FloatField()
    vendor_product = models.ForeignKey(Vendor_product,on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'order_detail'
        
class Vendor_product_images(models.Model):
    vendor_product = models.ForeignKey(Vendor_product, on_delete=models.CASCADE)
    vendor = models.ForeignKey(User,on_delete=models.CASCADE)
    image_url = models.ImageField()
    
    class Meta:
        db_table = 'vendor_product_images'
        
class Feedback(models.Model):
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=500)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    vendor = models.ForeignKey(Vendor_detail, on_delete=models.CASCADE)
    vendor_ans = models.CharField(max_length=500)
    admin_ans = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return self.title
    
    class Meta:
        db_table = 'feedback'
        
class Reviews(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    rating = models.FloatField(max_length=5,default=0.0)
    comment = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.user
    
    class Meta:
        db_table = 'review'
        

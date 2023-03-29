from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Brand)
admin.site.register(State)
admin.site.register(Vendor_detail)
admin.site.register(Vendor_product)
admin.site.register(Vendor_product_images)
admin.site.register(Status)
admin.site.register(Cart)
admin.site.register(Cart_detail)
admin.site.register(Order)
admin.site.register(Order_detail)
admin.site.register(Feedback)
admin.site.register(Reviews)
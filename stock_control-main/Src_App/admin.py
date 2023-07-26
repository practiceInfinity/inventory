from django.contrib import admin
from .models import * 



class Customer_Admin(admin.ModelAdmin):

    list_display = ['customer_code', 'customer_name']

class Product_Admin(admin.ModelAdmin):

    list_display = ['product_code', 'product_name']


admin.site.register(Customer, Customer_Admin)
admin.site.register(Product, Product_Admin)


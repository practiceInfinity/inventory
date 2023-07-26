from django.db import models
from django.contrib.auth.models import User



class Customer(models.Model):
    user = models.ForeignKey(to=User,on_delete=models.DO_NOTHING, null=True )
    customer_code = models.CharField(max_length=100)
    customer_name = models.CharField(max_length=100)
    customer_type = models.CharField(max_length=100)
    Sales_Person = models.CharField(max_length=100)
    Default_Delivery_Address = models.CharField(max_length=100)
    Default_Warehouse = models.CharField(max_length=100)
    notes = models.TextField()
    print_quote = models.BooleanField(default=False)
    print_invoice = models.BooleanField(default=False)
    print_packing_slip = models.BooleanField(default=False)
    Obselete = models.BooleanField(default=False)
    Stop_Credit = models.BooleanField(default=False)
    GST_Number = models.CharField(max_length=100, verbose_name='GST / VAT Number')
    Default_Currency = models.CharField(max_length=100)
    Taxable = models.BooleanField(default=False)
    Tax_Rate = models.CharField(max_length=100)
    Sales_Account = models.CharField(max_length=100)
    Bank_Account_Name = models.CharField(max_length=100)
    Bank_Account_Number = models.CharField(max_length=100)
    Payments_Terms = models.CharField(max_length=100)
    Sell_Price_Tier = models.CharField(max_length=100)
    Discount = models.CharField(max_length=20)

    def __str__(self):

        return self.customer_name



class Product(models.Model):

    user = models.ForeignKey(to=User, on_delete=models.DO_NOTHING, null=True)
    
    product_code = models.CharField(max_length=100)
    product_name = models.CharField(max_length=100)
    product_category = models.CharField(max_length=100)
    dealer = models.CharField(max_length=100)
    unit_of_measure = models.CharField(max_length=100)
    product_description = models.TextField()
    availability = models.BooleanField(default=False)
    delivery = models.BooleanField(default=False)
    deliver_charges = models.BooleanField(default=False)
    height = models.CharField(max_length=10)
    width = models.CharField(max_length=10)
    depth = models.CharField(max_length=10)
    is_premium = models.BooleanField(default=False)
    different_sizes = models.BooleanField(default=False)
    pack_size_category = models.CharField(max_length=100)
    previous_price = models.CharField(max_length=100)
    current_price = models.CharField(max_length=100)
    discount = models.CharField(max_length=100)


    def __str__(self):

        return self.product_name
    



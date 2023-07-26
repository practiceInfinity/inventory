from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import logout , login, authenticate
from .models import Customer, Product


@login_required(login_url='login')
def Home(request):

    return render(request, 'home.html')



# LOGIN EXISTING USERS 



def Login(request):
    context = {}
    message = None

    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, username=username, email=email, password=password)

        if user is not None:    

            login(request, user)
            return redirect('homepage')
        
        else: 
            context['message'] = 'Invalid credentials'

    return render(request, 'login.html', context)


#  REGISTER NEW USERS 

def Register(request):
    message = None
    context = {}

    if request.method == 'POST':
        full_name = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        context['username'] = full_name
        context['email'] = email


        if not User.objects.filter(email=email).exists():

            new_user = User.objects.create_user(
                username=full_name,
                email=email,
                password=password
            )
            new_user.save()
            return redirect('homepage')
        else:
            message = "Email already in Registered."
            context['messages'] = message

    return render(request, 'register.html', context)


def Add_Customer(request):
    context = {}


    current_user = request.user

    if request.method == 'POST':

        print_quote = request.POST.get('print-quote')
        print_invoice = request.POST.get('print-invoice')
        print_packing_slip = request.POST.get('print-packing-slip')
        obsolete = request.POST.get('obsolete')
        stop_credit = request.POST.get('stop-credit')
        taxable = request.POST.get('taxable')

        if print_quote == 'on':
            print_quote = True
        else:
            print_quote = False
            
        if print_invoice == 'on':
            print_invoice = True
        else:
            print_invoice = False
        if print_packing_slip == 'on':
            print_packing_slip = True
        else:
            print_packing_slip = False
        if obsolete == 'on':
            obsolete = True
        else:
            obsolete = False
        if stop_credit == 'on':
            stop_credit = True
        else:
            stop_credit = False
        if taxable == 'on':
            taxable = True
        else:
            taxable = False

        customer_code = request.POST['c-code']
        customer_name = request.POST['c-name']
        customer_type = request.POST['c-type']
        sales_person = request.POST['sales_person']
        default_delivery_address = request.POST['c-d-address']
        default_warehouse = request.POST['c-warehouse']
        notes = request.POST['notes']

        gst_number = request.POST['gst']
        default_currency = request.POST['default-currency']
        tax_rate = request.POST['tax-rate']
        sales_account = request.POST['sales-account']
        bank_account_name = request.POST['bank-account-name']
        bank_account_number = request.POST['bank-account-number']
        payment_terms = request.POST['payment-terms']
        sell_price_tier = request.POST['sell-price-tier']
        discount = request.POST['discount']

        # Check if the customer code is already taken
        if Customer.objects.filter(customer_code=customer_code).exists():
            context['message'] = 'Customer Code is already in use for another Customer.'
            return redirect('add_customer')  # Redirect back to the form with an error message

        customer = Customer.objects.create(
            user=current_user,
            customer_code=customer_code,
            customer_name=customer_name,
            customer_type=customer_type,
            Sales_Person=sales_person,
            Default_Delivery_Address=default_delivery_address,
            Default_Warehouse=default_warehouse,
            notes=notes,
            print_quote=print_quote,
            print_invoice=print_invoice,
            print_packing_slip=print_packing_slip,
            Obselete=obsolete,
            Stop_Credit=stop_credit,
            GST_Number=gst_number,
            Default_Currency=default_currency,
            Taxable=taxable,
            Tax_Rate=tax_rate,
            Sales_Account=sales_account,
            Bank_Account_Name=bank_account_name,
            Bank_Account_Number=bank_account_number,
            Payments_Terms=payment_terms,
            Sell_Price_Tier=sell_price_tier,
            Discount=discount,
        )

        customer.save()

        messages.success(request, f"Customer '{customer.customer_code}' created successfully.")

        return redirect('homepage')

    return render(request, 'add_customer.html')


def Customers(request):
    context = {}
    current_user = request.user 
    customers = None
    try:
        customers = Customer.objects.filter(user=current_user)
        if customers is not None:
            context['customers'] = customers
        else:
            context['message'] = "You don't have any customers yet."

    except Exception as e:
        print(e)


    return render(request, 'customers.html', context)


def Add_Product(request):

    context = {}

    if request.method == 'POST':
        # Get the form data from the request
        product_code = request.POST.get('product_code')
        product_name = request.POST.get('product_name')
        product_category = request.POST.get('product_category')
        dealer = request.POST.get('dealer')
        unit_of_measure = request.POST.get('unit_of_measure')
        product_description = request.POST.get('product_description')
        availability = request.POST.get('availability')
        delivery = request.POST.get('delivery')
        delivery_charges = request.POST.get('delivery_charges')
        height = request.POST.get('height')
        width = request.POST.get('width')
        depth = request.POST.get('depth')
        is_premium = request.POST.get('is_premium')
        different_sizes = request.POST.get('different_sizes')
        pack_size_category = request.POST.get('pack_size_category')
        previous_price = request.POST.get('previous_price')
        current_price = request.POST.get('current_price')
        discount = request.POST.get('discount')
    
        if availability == 'on':
            availability = True
        else:
            availability = False
        if delivery == 'on':
            delivery = True
        else:
            delivery = False
        
        if delivery_charges == 'on':
            delivery_charges = True
        else:
            delivery_charges = False
        
        if is_premium == 'on':
            is_premium = True
        else:
            is_premium = False
        
        if different_sizes == 'on':
            different_sizes = True
        else:
            different_sizes = False

        if Product.objects.filter(product_code=product_code).exists():
            context['message'] = 'Product Code is already in use by another product.'
            return redirect('add_product')
            
        product = Product(
            product_code=product_code,
            product_name=product_name,
            product_category=product_category,
            dealer=dealer,
            unit_of_measure=unit_of_measure,
            product_description=product_description,
            availability=availability,
            delivery=delivery,
            deliver_charges=delivery_charges,
            height=height,
            width=width,
            depth=depth,
            is_premium=is_premium,
            different_sizes=different_sizes,
            pack_size_category=pack_size_category,
            previous_price=previous_price,
            current_price=current_price,
            discount=discount,
        )

        # Save the Product object to the database
        product.save()

        return redirect('products')

    return render(request, 'add_product.html', context)

def Products(request):

    context = {}
    current_user = request.user
        
    try:
        products = Product.objects.filter(user=current_user)
        context['products'] = products
        print(products)


    except Exception as E: 
        print(E)

    return render(request, 'products.html', context)

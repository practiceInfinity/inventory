from django.urls import path 
from . import views


urlpatterns = [
    path('', views.Home, name='homepage'),
    path('login/', views.Login, name='login'),
    path('register/', views.Register, name='register'),
    path('add_customer/', views.Add_Customer, name='add_customer'),
    path('customers/', views.Customers, name='customers'),
    path('add_product/', views.Add_Product,name='add_product'),
    path('products/',views.Products, name='products'),
]


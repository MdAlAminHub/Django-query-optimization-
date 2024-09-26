from django.contrib import admin

# Register your models here.
from .models import Customer,Product,Order,OrderItem

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name','email')

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','price')    

@admin.register(Order)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('customer',)      

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order','product')     
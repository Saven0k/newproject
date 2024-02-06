from django.contrib import admin
from .models import Client, Product, Order
# Register your models here.


class ClientAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'number_phone']
    ordering = ['name', '-date_of_register']
    list_filter = ['name', 'date_of_register']
    search_fields = ['number_phone']
    search_help_text = 'Поиск по полю номер телефона(number_phone)'
    
    readonly_fields = ['date_of_register']

    fieldsets = [
        (
            'Client',
            {
                'classes':['wide'],
                'fields':['name', 'number_phone'],
            },
        ),
        (
            'Details',
            {
                'classes': ['collapse'],
                'description':'address',
                'fields': ['date_of_register'],
            },
        ),
        (
            'Other',
            {
                'description': 'Контактная информация',
                'fields': ['email'] 
            }
        )
    ]
    
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'discription', 'date_of_add', 'cost']
    ordering = ['title', '-date_of_add']
    list_filter = ['title', 'date_of_add']
    search_fields = ['title']
    search_help_text = 'Поиск по полю название продукта'
    
    # readonly_fields = ['date_of_add']
     
    fieldsets = [
        (
            'Product',
            {
                'classes':['wide'],
                'fields':['title', 'cost']
            },
        ),
        (
            'Details',
            {
                'classes': ['collapse'],
                'description':'Описание  продукта ',
                'fields': ['discription', 'date_of_add'],
            },
        ),
        (
            'Other',
            {
                'description': 'Прочая информация',
                'fields': ['amount_product'] 
            }
        )
    ]
    

class OrderAdmin(admin.ModelAdmin):
    list_display = ['client', 'product', 'date_of_create', 'total_cost']
    ordering = ['client', '-date_of_create']
    list_filter = ['client', 'date_of_create']
    search_fields = ['client']
    search_help_text = 'Поиск по полю клиент'
    
    readonly_fields = ['date_of_create']
     
    fieldsets = [
        (
            'Order',
            {
                'classes':['wide'],
                'fields':['client', 'total_cost']
            },
        ),
        (
            'Details',
            {
                'classes': ['collapse'],
                'description':'Список продуктов в заказе ',
                'fields': ['product'],
            },
        ),
    ]    
    

admin.site.register(Client, ClientAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)

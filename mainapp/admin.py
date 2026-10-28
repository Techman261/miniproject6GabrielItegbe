# INF601
# Gabriel Itegbe
# Advanced Programming in Python
# Mini Project 6

from django.contrib import admin
from .models import Product, WishlistItem

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category', 'created_at')
    list_filter = ('category', 'created_at')
    search_fields = ('name', 'description')
    ordering = ('-created_at',)

@admin.register(WishlistItem)
class WishlistItemAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'added_at')
    list_filter = ('added_at', 'user')
    search_fields = ('user_username', 'product_name')
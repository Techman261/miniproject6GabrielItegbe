# INF601
# Gabriel Itegbe
# Advanced Programming in Python
# Mini Project 6

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Product, WishlistItem
from django.contrib.admin.views.decorators import staff_member_required
from .forms import ProductForm

@staff_member_required
def admin_dashboard_view(request):
    products = Product.objects.all().order_by('-created_at')
    return render(request, 'mainapp/admin_dashboard.html', {'products': products})

@staff_member_required
def admin_add_product_view(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_dashboard')
    else:
        form = ProductForm()
    return render(request, 'mainapp/admin_product_form.html', {'form': form, 'action': 'Add'})

@staff_member_required
def admin_edit_product_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('admin_dashboard')
    else:
        form = ProductForm(instance=product)
    return render(request, 'mainapp/admin_product_form.html', {'form': form, 'action': 'Edit'})

@staff_member_required
def admin_delete_product_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('admin_dashboard')
    return render(request, 'mainapp/admin_product_confirm_delete.html', {'product': product})

def home_view(request):
    featured_products = Product.objects.all().order_by('-created_at')[:4]
    return render(request, 'mainapp/home.html', {'products': featured_products})

def product_list_view(request):
    products = Product.objects.all().order_by('-created_at')
    return render(request, 'mainapp/product_list.html', {'products': products})

def product_detail_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    is_in_wishlist = False
    if request.user.is_authenticated:
        is_in_wishlist = WishlistItem.objects.filter(user=request.user, product=product).exists()
    return render(request, 'mainapp/product_detail.html', {'product': product, 'is_in_wishlist': is_in_wishlist})

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'mainapp/register.html', {'form': form})

@login_required
def wishlist_view(request):
    wishlist_items = WishlistItem.objects.filter(user=request.user).select_related('product')
    return render(request, 'mainapp/wishlist.html', {'wishlist_items': wishlist_items})

@login_required
def toggle_wishlist_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    wishlist_item, created = WishlistItem.objects.get_or_create(user=request.user, product=product)
    if not created:
        wishlist_item.delete()
    return redirect('product_detail', pk=pk)
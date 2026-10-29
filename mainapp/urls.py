from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('products/', views.product_list_view, name='product_list'),
    path('products/<int:pk>/', views.product_detail_view, name='product_detail'),
    path('register/', views.register_view, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='mainapp/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('wishlist/', views.wishlist_view, name='wishlist'),
    path('wishlist/toggle/<int:pk>/', views.toggle_wishlist_view, name='toggle_wishlist'),
    path('my-admin/', views.admin_dashboard_view, name='admin_dashboard'),
    path('my-admin/add/', views.admin_add_product_view, name='admin_add_product'),
    path('my-admin/edit/<int:pk>/', views.admin_edit_product_view, name='admin_edit_product'),
    path('my-admin/delete/<int:pk>/', views.admin_delete_product_view, name='admin_delete_product'),
]
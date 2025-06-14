from django.urls import path
from . import views

urlpatterns = [
    path("products/", views.products, name="products"),
    path("product_detail/<slug:slug>/", views.product_detail, name="product_detail"),
    path("add_item/", views.add_items, name="add_item"),
    path("product_in_cart/", views.product_in_cart, name="product_in_cart"),
    path("get_cart_stat/", views.get_cart_stat, name="get_cart_stat"),
    path("get_cart/", views.get_cart, name="get_cart"),
    path("update_quantity/", views.update_quantity, name="update_quantity"),
    path("delete_items/", views.delete_items, name="delete_items"),
    path("get_username/", views.get_username, name="get_username"),
    path("user_info/", views.user_info, name="user_info"),
]

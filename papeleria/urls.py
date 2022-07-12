from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("log-out", views.logout_view, name="log-out"),
    path("maintenance", views.maintenance, name="maintenance"),
    path("list_customers", views.list_customers, name="list-customers"),
    path("list_products", views.list_products, name="list-products"),
    path("list_sellers", views.list_sellers, name="list-sellers"),
    path("list_users", views.list_users, name="list-users"),
    path("add_customer", views.add_customer, name="add-customer"),
    path("add_customer_view", views.add_customer_view, name="add-customer-view"),
    path("add_product", views.add_product, name="add-product"),
    path("add_product_view", views.add_product_view, name="add-product-view"),
    path("add_user", views.add_user, name="add-user"),
    path("add_user_view", views.add_user_view, name="add-user-view"),
    path("register", views.register, name="register"),
]
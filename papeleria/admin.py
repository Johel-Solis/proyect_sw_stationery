from django.contrib import admin
from .models import Bill, Category, Customer, Person, Product, SaleDetail, User

admin.site.register(Bill)
admin.site.register(Category)
admin.site.register(Customer)
admin.site.register(Person)
admin.site.register(Product)
admin.site.register(SaleDetail)
admin.site.register(User)


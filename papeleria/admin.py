from django.contrib import admin
from .models import Person, Product, User, Customer

admin.site.register(Person)
admin.site.register(Product)
admin.site.register(User)
admin.site.register(Customer)

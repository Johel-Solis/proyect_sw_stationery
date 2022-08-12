from django import forms
from .models import Category, Customer, Person, Product, User, SaleDetail

class NewProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('reference', 'category', 'name', 'stock', 'brand', 'purchase_price', 'sale_price', 'description')
        labels = {
            "reference":  "Referencia",
            "category":  "Categoria",
            "name": "Nombre",
            "stock": "Existencias",
            "brand": "Marca",
            "purchase_price": "Precio compra",
            "sale_price": "Precio venta",
            "description": "Descripción"
        }

class NewUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password')
        labels = {
            "username": "Nombre usuario",
            "password": "Clave"
            
        }

class NewPersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ('id', 'name', 'surname', 'email', 'phone', 'birthday')
        labels = {
            "id":  "Cedula",
            "name": "Nombres",
            "surname": "Apellidos",
            "email": "Correo",
            "phone": "Teléfono",
            "birthday": "Fecha nacimiento"
        }

class NewCustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('id', 'name', 'phone', 'email')
        labels = {
            "id":  "Cedula o Nit",
            "name": "Nombre",
            "phone": "Teléfono",
            "email": "Correo"
        }

class SearchProductForm(forms.Form):
    reference = forms.IntegerField()

class SetPersonForm(forms.Form):
    id = forms.IntegerField(required=False)

class NewSaleDetailForm(forms.ModelForm):
    class Meta:
        model = SaleDetail
        fields = ('product', 'quantity', 'unit_price')
        labels = {
            "product":  "Nombre producto",
            "quantity": "Unidades",
            "unit_price": "Precio unitario"
        }
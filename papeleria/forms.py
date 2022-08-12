from tkinter import Widget
from django import forms
from .models import Category, Customer, Person, Product, User, SaleDetail

class NewProductForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control'
            form.field.widget.attrs['placeholder'] = form.label
            form.field.widget.attrs['style'] = 'margin-left: 0px;width: 100%;'

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
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control'
            form.field.widget.attrs['placeholder'] = form.label
            form.field.widget.attrs['style'] = 'margin-left: 0px;width: 100%;'

    class Meta:
        model = User
        fields = ('username', 'password')
        labels = {
            "username": "Nombre usuario",
            "password": "Contraseña" 
        }
        widgets = {
            'username': forms.TextInput(attrs={'pattern': '[a-zA-Z0-9]+', 'title': 'Solo se permiten letras y números'}),
            'password': forms.PasswordInput()
               }


class NewPersonForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control'
            form.field.widget.attrs['placeholder'] = form.label
            form.field.widget.attrs['style'] = 'margin-left: 0px;width: 100%;'
              
    class Meta:
        model = Person
        fields = ('id', 'name', 'surname', 'email', 'phone', 'birthday')
        labels = {
            "id":  "Cedula",
            "name": "Nombres",
            "surname": "Apellidos",
            "email": "Correo electrónico",
            "phone": "Teléfono",
            "birthday": "Fecha nacimiento"
        }
        widgets = {
            'birthday': forms.DateInput(attrs={'type': 'date','format':'%d/%m/%Y'})
               }

class NewCustomerForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control'
            form.field.widget.attrs['placeholder'] = form.label
            form.field.widget.attrs['style'] = 'margin-left: 0px;width: 100%;'
        
    class Meta:
        model = Customer
        fields = ('id', 'name', 'phone', 'email')
        labels = {
            "id":  "Cedula o Nit",
            "name": "Nombre",
            "phone": "Teléfono",
            "email": "Correo electrónico"
        }
       

class SearchProductForm(forms.Form):
    reference = forms.IntegerField()

class SetPersonForm(forms.Form):
<<<<<<< HEAD
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control'
            form.field.widget.attrs['placeholder'] = form.label
            form.field.widget.attrs['style'] = 'margin-left: 0px;width: 100%;'

    id = forms.IntegerField(required=False)

=======
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
>>>>>>> 4a6cf621923c9e85256ff5da92ca02aa233fbc66

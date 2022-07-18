from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt
from django.db import IntegrityError
from django.db import transaction
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.http import JsonResponse
import json
from django.urls import reverse
from django.shortcuts import redirect
from django.contrib import messages

from .models import Bill, Customer, Person, Product, SaleDetail, User
from .forms import NewCustomerForm, NewPersonForm, NewProductForm, NewUserForm

# TODO:
# Nothing

@csrf_exempt
@login_required
def add_admin(request):
    if request.method == "POST":
        try:
            newUserForm = NewUserForm(request.POST)
            newPersonForm = NewPersonForm(request.POST)
            
            if newUserForm.is_valid() and newPersonForm.is_valid():
                username = request.POST["username"]
                password = request.POST["password"]
                identification = request.POST["id"]
                name = request.POST["name"]
                surname= request.POST["surname"]
                email = None if request.POST["email"] == "" else request.POST["email"]
                phone = None if request.POST["phone"] == "" else request.POST["phone"]
                birthday = None if request.POST["birthday"] == "" else request.POST["birthday"]

                user =  User.objects.create_user(
                    username=username,
                    password=password,
                    user_type="admin"
                )
                user.save()

                person = Person(
                    user=user,
                    id=identification,
                    name=name,
                    surname=surname,
                    email=email,
                    phone=phone,
                    birthday=birthday
                )
                person.save()
                messages.success(request, 'El administrador se creó exitosamente')
            else:
                return render(request, "admin/add.html", {
                    "newUserForm": newUserForm,
                    "newPersonForm": newPersonForm
                })
        except Exception as e:
            transaction.rollback()
            print(e)
            messages.error(request, 'Se produjo un error. El administrador no pudo ser creado')
    else:
        messages.error(request, 'La petición no es válida. El administrador no pudo ser creado')
    
    return redirect("list-admins")

@csrf_exempt
@login_required
def add_admin_view(request):
    return render(request, "admin/add.html", {
        "newUserForm": NewUserForm(),
        "newPersonForm": NewPersonForm()
    })

@csrf_exempt
@login_required
def add_customer(request):
    if request.method == "POST":
        try:
            newCustomerForm = NewCustomerForm(request.POST)
            
            if newCustomerForm.is_valid():
                identification = request.POST["id"]
                name = request.POST["name"]
                email = None if request.POST["email"] == "" else request.POST["email"]
                phone = None if request.POST["phone"] == "" else request.POST["phone"]

                customer = Customer(
                    id=identification,
                    name=name,
                    email=email,
                    phone=phone)
                
                customer.save()
                messages.success(request, 'El cliente se creó exitosamente')
            else:
                return render(request, "customer/add.html", {
                    "newCustomerSForm": newCustomerForm
                })
        except Exception as e:
            print(e)
            messages.error(request, 'Se produjo un error. El cliente no pudo ser creado')
    else:
        messages.error(request, 'La petición no es válida. El cliente no pudo ser creado')
    
    return redirect("list-customers")

@csrf_exempt
@login_required
def add_customer_view(request):
    return render(request, "customer/add.html", {
        "newCustomerForm": NewCustomerForm()
    })

@csrf_exempt
@login_required
def add_product(request):
    if request.method == "POST":
        try:
            newProductForm = NewProductForm(request.POST)
            
            if newProductForm.is_valid():
                reference = request.POST["reference"]
                name = request.POST["name"]
                stock = request.POST["stock"]
                brand = request.POST["brand"]
                purchasePrice = request.POST["purchase_price"]
                salePrice = request.POST["sale_price"]
                description = request.POST["description"]
                
                product = Product(
                    reference=reference,
                    name=name,
                    stock=stock,
                    brand=brand,
                    purchase_price=purchasePrice,
                    sale_price=salePrice,
                    description=description).save()

                messages.success(request, 'El producto se creó exitosamente')
            else:
                return render(request, "product/add.html", {
                    "newProductForm": newProductForm
                })
        except Exception as e:
            print(e)
            messages.error(request, 'Se produjo un error. El producto no pudo ser creado')
    else:
        messages.error(request, 'La petición no es válida. El producto no pudo ser creado')
    
    return redirect("list-products")

@csrf_exempt
@login_required
def add_product_view(request):
    return render(request, "product/add.html", {
        "newProductForm": NewProductForm()
    })

@csrf_exempt
@login_required
def add_seller(request):
    if request.method == "POST":
        try:
            newUserForm = NewUserForm(request.POST)
            newPersonForm = NewPersonForm(request.POST)
            
            if newUserForm.is_valid() and newPersonForm.is_valid():
                username = request.POST["username"]
                password = request.POST["password"]
                identification = request.POST["id"]
                name = request.POST["name"]
                surname= request.POST["surname"]
                email = None if request.POST["email"] == "" else request.POST["email"]
                phone = None if request.POST["phone"] == "" else request.POST["phone"]
                birthday = None if request.POST["birthday"] == "" else request.POST["birthday"]

                user =  User.objects.create_user(
                    username=username,
                    password=password,
                    user_type="vendedor"
                )
                user.save()

                person = Person(
                    user=user,
                    id=identification,
                    name=name,
                    surname=surname,
                    email=email,
                    phone=phone,
                    birthday=birthday
                )
                person.save()
                messages.success(request, 'El vendedor se creó exitosamente')
            else:
                return render(request, "seller/add.html", {
                    "newUserForm": newUserForm,
                    "newPersonForm": newPersonForm
                })
        except Exception as e:
            transaction.rollback()
            print(e)
            messages.error(request, 'Se produjo un error. El vendedor no pudo ser creado')
    else:
        messages.error(request, 'La petición no es válida. El vendedor no pudo ser creado')
    
    return redirect("list-sellers")

@csrf_exempt
@login_required
def add_seller_view(request):
    return render(request, "seller/add.html", {
        "newUserForm": NewUserForm(),
        "newPersonForm": NewPersonForm()
    })

@csrf_exempt
@login_required
def edit_product(request, reference):
    if request.method == "POST":
        try:
            product = Product.objects.get(reference=reference)
            newProductForm = newProductForm(request.POST, instance=product)

            if newProductForm.is_valid():
                reference = request.POST["reference"]
                name = request.POST["name"]
                stock = request.POST["stock"]
                brand = request.POST["brand"]
                purchasePrice = request.POST["purchase_price"]
                salePrice = request.POST["sale_price"]
                description = request.POST["description"]

                if product:
                    product.reference=reference
                    product.name=name
                    product.stock=stock
                    product.brand=brand
                    product.purchase_price=purchasePrice
                    product.sale_price=salePrice
                    product.description=description
                    product.save()

                    messages.success(request, 'El producto se editó exitosamente')
            else:
                return render(request, "product/new.html", {
                    "newProductForm": newProductForm
                })
        except Exception as e:
            print(e)
            messages.error(request, 'Se produjo un error. El producto no pudo ser editado')
    else:
        messages.error(request, 'La petición no es válida. El producto no pudo ser editado')
    
    return redirect("list-products")

@csrf_exempt
@login_required
def edit_product_view(request, reference):
    product = Product.objects.get(reference=reference)
    editProductForm = NewProductForm(instance=product)

    return render(request, "product/edit.html", {
        "editProductForm": editProductForm
    })

@csrf_exempt
@login_required
def delete_admin(request, id):
    if request.method == "DELETE":
        try:
            admin = User.objects.filter(id=id)

            if admin:
                admin.delete()
                return JsonResponse({"message": "Administrador eliminado"}, status=201)
            else:
                return JsonResponse({"message": "El administrador no existe"}, status=201)
        except Exception as e:
            transaction.rollback()
            print(e)
    
    return JsonResponse({"message": "Administrador no eliminado"}, status=201)

@csrf_exempt
@login_required
def delete_customer(request, id):
    if request.method == "DELETE":
        try:
            customer = Customer.objects.filter(id=id)

            if customer:
                customer.delete()
                return JsonResponse({"message": "Cliente eliminado"}, status=201)
            else:
                return JsonResponse({"message": "El cliente no existe"}, status=201)
        except Exception as e:
            transaction.rollback()
            print(e)
    
    return JsonResponse({"message": "Cliente no eliminado"}, status=201)

@csrf_exempt
@login_required
def delete_product(request, reference):
    if request.method == "DELETE":
        try:
            product = Product.objects.filter(reference=reference)

            if product:
                product.delete()
                return JsonResponse({"message": "Producto eliminado"}, status=201)
            else:
                return JsonResponse({"message": "El producto no existe"}, status=201)
        except Exception as e:
            transaction.rollback()
            print(e)
    
    return JsonResponse({"message": "Producto no eliminado"}, status=201)


@csrf_exempt
@login_required
def delete_seller(request, id):
    if request.method == "DELETE":
        try:
            seller = User.objects.filter(id=id)

            if seller:
                seller.delete()
                return JsonResponse({"message": "Vendedor eliminado"}, status=201)
            else:
                return JsonResponse({"message": "El vendedor no existe"}, status=201)
        except Exception as e:
            transaction.rollback()
            print(e)
    
    return JsonResponse({"message": "Vendedor no eliminado"}, status=201)

def index(request):
    if request.user.is_authenticated:
        return render(request, "general/index.html")
    else:
        return HttpResponseRedirect(reverse("login"))

@csrf_exempt
@login_required
def list_admins(request):
    admins = User.objects.all().filter(user_type="admin")
    
    return render(request, "admin/list.html", {
        "admins": admins
    })

@csrf_exempt
@login_required
def list_customers(request):
    customers = Customer.objects.all()

    return render(request, "customer/list.html", {
        "customers": customers
    })

@csrf_exempt
@login_required
def list_products(request):
    products = Product.objects.all()

    return render(request, "product/list.html", {
        "products": products
    })

@csrf_exempt
@login_required
def list_sellers(request):
    sellers = User.objects.all().filter(user_type="vendedor")
    
    return render(request, "seller/list.html", {
        "sellers": sellers
    })

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)

            return HttpResponseRedirect(reverse("index"))
        else:
            messages.error(request, "Usuario o contraseña invalido.")
            return render(request, "general/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "general/login.html")

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("login"))

def maintenance(request):
    return render(request, "general/maintenance.html")

def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "general/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "general/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "general/register.html")
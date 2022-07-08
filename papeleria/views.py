from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt
from django.db import IntegrityError
from django.db import transaction
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import redirect
from django.contrib import messages

from .models import Bill, Person, Product, SaleDetail, User
from .forms import NewPersonForm, NewProductForm, NewUserForm

def index(request):
    if request.user.is_authenticated:
        return render(request, "general/index.html")
    else:
        return HttpResponseRedirect(reverse("login"))

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
    sellers = User.objects.all().filter(is_seller=True)
    
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
                purchasePrice = request.POST["purchase_price"]
                salePrice = request.POST["sale_price"]
                
                product = Product(
                    reference=reference,
                    name=name,
                    stock=stock, 
                    purchase_price=purchasePrice,
                    sale_price=salePrice).save()

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
                is_admin = True if "is_admin" in request.POST else False
                is_seller = True if "is_seller" in request.POST else False
                identification = request.POST["id"]
                name = request.POST["name"]
                surname= request.POST["surname"]
                email = None if request.POST["email"] == "" else request.POST["email"]
                phone = None if request.POST["phone"] == "" else request.POST["phone"]
                birthday = None if request.POST["birthday"] == "" else request.POST["birthday"]

                previousPerson = Person.objects.all().filter(id=identification)

                # TODO: Make sure that at least one checkbox is selected
                # Create a custom message validion for this validation (Raise a validation failure)
                # Add marca to product

                if previousPerson and previousPerson.is_seller:
                    return render(request, "seller/add.html", {
                        "formValidationMessage": "La cedula ya esta registrada con otro usuario",
                        "newUserForm": newUserForm,
                        "newPersonForm": newPersonForm
                    })

                user = User(
                    username=username,
                    password=password,
                    is_admin=is_admin,
                    is_seller=is_seller)
                
                user.save()

                person = Person(
                    user=user,
                    id=identification,
                    name=name,
                    surname=surname,
                    email=email,
                    phone=phone,
                    birthday=birthday)
                
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
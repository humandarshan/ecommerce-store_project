from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import Http404
from .models import Product, Order, OrderItem


def home(request):
    context = {
        "electronics": Product.objects.filter(category="electronics"),
        "fashion": Product.objects.filter(category="fashion"),
        "perfumes": Product.objects.filter(category="perfumes"),
        "home_accessories": Product.objects.filter(category="home"),
    }
    return render(request, "store/home.html", context)


def products(request):
    return render(request, "store/products.html", {"products": Product.objects.all()})


def product_detail(request, product_id):
    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist:
        raise Http404("Product not found")
    return render(request, "store/product.html", {"product": product})


def add_to_cart(request, product_id):
    cart = request.session.get("cart", {})
    key = str(product_id)
    cart[key] = cart.get(key, 0) + 1
    request.session["cart"] = cart
    return redirect("home")


def increase_qty(request, product_id):
    cart = request.session.get("cart", {})
    key = str(product_id)
    if key in cart:
        cart[key] += 1
        request.session["cart"] = cart
    return redirect("cart")


def decrease_qty(request, product_id):
    cart = request.session.get("cart", {})
    key = str(product_id)
    if key in cart:
        cart[key] -= 1
        if cart[key] <= 0:
            del cart[key]
        request.session["cart"] = cart
    return redirect("cart")


def remove_from_cart(request, product_id):
    cart = request.session.get("cart", {})
    key = str(product_id)
    if key in cart:
        del cart[key]
        request.session["cart"] = cart
    return redirect("cart")


def _get_cart_items(request):
    cart_data = request.session.get("cart", {})
    items = []
    total = 0
    for pid, qty in cart_data.items():
        try:
            product = Product.objects.get(id=int(pid))
        except Product.DoesNotExist:
            continue
        subtotal = product.price * qty
        items.append({
            "id": product.id,
            "name": product.name,
            "price": product.price,
            "qty": qty,
            "subtotal": subtotal,
        })
        total += subtotal
    return items, total


def cart(request):
    items, total = _get_cart_items(request)
    return render(request, "store/cart.html", {"products": items, "total": total})


def checkout(request):
    items, total = _get_cart_items(request)

    if not items:
        return redirect("cart")

    if request.method == "POST":
        name = request.POST.get("name", "")
        email = request.POST.get("email", "")
        address = request.POST.get("address", "")

        order = Order.objects.create(
            user=request.user if request.user.is_authenticated else None,
            name=name,
            email=email,
            address=address,
            total=total,
        )
        for item in items:
            OrderItem.objects.create(
                order=order,
                product_name=item["name"],
                price=item["price"],
                quantity=item["qty"],
            )

        request.session["cart"] = {}
        return render(request, "store/checkout_success.html", {
            "order_number": order.id,
            "name": name,
        })

    return render(request, "store/checkout.html", {"products": items, "total": total})


def login_view(request):
    error = None
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        user = None
        try:
            user_obj = User.objects.get(email=email)
            user = authenticate(request, username=user_obj.username, password=password)
        except User.DoesNotExist:
            user = None

        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            error = "Invalid email or password."

    return render(request, "store/login.html", {"error": error})


def register(request):
    error = None
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        password = request.POST.get("password")

        if User.objects.filter(username=name).exists():
            error = "That name is already taken."
        elif User.objects.filter(email=email).exists():
            error = "An account with this email already exists."
        else:
            user = User.objects.create_user(username=name, email=email, password=password)
            login(request, user)
            return redirect("home")

    return render(request, "store/register.html", {"error": error})


def logout_view(request):
    logout(request)
    return redirect("home")
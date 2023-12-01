from django.shortcuts import (
    render,
    redirect,
    HttpResponse,
    HttpResponseRedirect,
)
from .models import *
from django.contrib.auth.hashers import check_password, make_password
from django import template

from .forms import commentForm

from base.middlewares.auth import auth_middleware

from django.contrib.auth.decorators import login_required


# Create your views here.


# def home(request):
#     context = {}
#     return render(request, "base/home.html", context)


def home(request):
    context = {}
    return render(request, "base/home.html", context)


def trekingHiking(request):
    if request.method == "GET":
        cart = request.session.get("cart")
        if not cart:
            request.session["cart"] = {}
        products = Product.get_all_products()[0:21]
        data = {}
        data["products"] = products
        return render(request, "base/trekingHiking.html", data)

    else:
        product = request.POST.get("product")
        remove = request.POST.get("remove")
        cart = request.session.get("cart")
        if cart:
            quantity = cart.get(product)
            if quantity:
                if remove:
                    if quantity == 1:
                        cart.pop(product)
                    else:
                        cart[product] = quantity - 1
                else:
                    cart[product] = quantity + 1
            else:
                cart[product] = 1
        else:
            cart = {}
            cart[product] = 1

        request.session["cart"] = cart

        return redirect("trekingHiking")


def accessories(request):
    if request.method == "GET":
        cart = request.session.get("cart")
        if not cart:
            request.session["cart"] = {}
        products = Product.get_all_products()[102:109]
        data = {}
        data["products"] = products
        return render(request, "base/accessories.html", data)

    else:
        product = request.POST.get("product")
        remove = request.POST.get("remove")
        cart = request.session.get("cart")
        if cart:
            quantity = cart.get(product)
            if quantity:
                if remove:
                    if quantity == 1:
                        cart.pop(product)
                    else:
                        cart[product] = quantity - 1
                else:
                    cart[product] = quantity + 1
            else:
                cart[product] = 1
        else:
            cart = {}
            cart[product] = 1

        request.session["cart"] = cart

        return redirect("accessories")


def equipments(request):
    if request.method == "GET":
        cart = request.session.get("cart")
        if not cart:
            request.session["cart"] = {}
        products = Product.get_all_products()[21:28]
        data = {}
        data["products"] = products
        return render(request, "base/equipments.html", data)

    else:
        product = request.POST.get("product")
        remove = request.POST.get("remove")
        cart = request.session.get("cart")
        if cart:
            quantity = cart.get(product)
            if quantity:
                if remove:
                    if quantity == 1:
                        cart.pop(product)
                    else:
                        cart[product] = quantity - 1
                else:
                    cart[product] = quantity + 1
            else:
                cart[product] = 1
        else:
            cart = {}
            cart[product] = 1

        request.session["cart"] = cart

        return redirect("equipments")


def fitness(request):
    if request.method == "GET":
        cart = request.session.get("cart")
        if not cart:
            request.session["cart"] = {}
        products = Product.get_all_products()[28:41]
        data = {}
        data["products"] = products
        return render(request, "base/fitness.html", data)

    else:
        product = request.POST.get("product")
        remove = request.POST.get("remove")
        cart = request.session.get("cart")
        if cart:
            quantity = cart.get(product)
            if quantity:
                if remove:
                    if quantity == 1:
                        cart.pop(product)
                    else:
                        cart[product] = quantity - 1
                else:
                    cart[product] = quantity + 1
            else:
                cart[product] = 1
        else:
            cart = {}
            cart[product] = 1

        request.session["cart"] = cart

        return redirect("fitness")


def bags(request):
    if request.method == "GET":
        cart = request.session.get("cart")
        if not cart:
            request.session["cart"] = {}
        products = Product.get_all_products()[41:49]
        data = {}
        data["products"] = products
        return render(request, "base/bags.html", data)

    else:
        product = request.POST.get("product")
        remove = request.POST.get("remove")
        cart = request.session.get("cart")
        if cart:
            quantity = cart.get(product)
            if quantity:
                if remove:
                    if quantity == 1:
                        cart.pop(product)
                    else:
                        cart[product] = quantity - 1
                else:
                    cart[product] = quantity + 1
            else:
                cart[product] = 1
        else:
            cart = {}
            cart[product] = 1

        request.session["cart"] = cart

        return redirect("bags")


def racketSports(request):
    if request.method == "GET":
        cart = request.session.get("cart")
        if not cart:
            request.session["cart"] = {}
        products = Product.get_all_products()[49:60]
        data = {}
        data["products"] = products
        return render(request, "base/racketSports.html", data)

    else:
        product = request.POST.get("product")
        remove = request.POST.get("remove")
        cart = request.session.get("cart")
        if cart:
            quantity = cart.get(product)
            if quantity:
                if remove:
                    if quantity == 1:
                        cart.pop(product)
                    else:
                        cart[product] = quantity - 1
                else:
                    cart[product] = quantity + 1
            else:
                cart[product] = 1
        else:
            cart = {}
            cart[product] = 1

        request.session["cart"] = cart

        return redirect("racketSports")


def footwear(request):
    if request.method == "GET":
        cart = request.session.get("cart")
        if not cart:
            request.session["cart"] = {}
        products = Product.get_all_products()[60:70]
        data = {}
        data["products"] = products
        return render(request, "base/footwear.html", data)

    else:
        product = request.POST.get("product")
        remove = request.POST.get("remove")
        cart = request.session.get("cart")
        if cart:
            quantity = cart.get(product)
            if quantity:
                if remove:
                    if quantity == 1:
                        cart.pop(product)
                    else:
                        cart[product] = quantity - 1
                else:
                    cart[product] = quantity + 1
            else:
                cart[product] = 1
        else:
            cart = {}
            cart[product] = 1

        request.session["cart"] = cart

        return redirect("footwear")


def runningWalking(request):
    if request.method == "GET":
        cart = request.session.get("cart")
        if not cart:
            request.session["cart"] = {}
        products = Product.get_all_products()[70:78]
        data = {}
        data["products"] = products
        return render(request, "base/runningWalking.html", data)

    else:
        product = request.POST.get("product")
        remove = request.POST.get("remove")
        cart = request.session.get("cart")
        if cart:
            quantity = cart.get(product)
            if quantity:
                if remove:
                    if quantity == 1:
                        cart.pop(product)
                    else:
                        cart[product] = quantity - 1
                else:
                    cart[product] = quantity + 1
            else:
                cart[product] = 1
        else:
            cart = {}
            cart[product] = 1

        request.session["cart"] = cart

        return redirect("runningWalking")


def teamSports(request):
    if request.method == "GET":
        cart = request.session.get("cart")
        if not cart:
            request.session["cart"] = {}
        products = Product.get_all_products()[78:91]
        data = {}
        data["products"] = products
        return render(request, "base/teamSports.html", data)

    else:
        product = request.POST.get("product")
        remove = request.POST.get("remove")
        cart = request.session.get("cart")
        if cart:
            quantity = cart.get(product)
            if quantity:
                if remove:
                    if quantity == 1:
                        cart.pop(product)
                    else:
                        cart[product] = quantity - 1
                else:
                    cart[product] = quantity + 1
            else:
                cart[product] = 1
        else:
            cart = {}
            cart[product] = 1

        request.session["cart"] = cart

        return redirect("teamSports")


def leisureItems(request):
    if request.method == "GET":
        cart = request.session.get("cart")
        if not cart:
            request.session["cart"] = {}
        products = Product.get_all_products()[91:102]
        data = {}
        data["products"] = products
        return render(request, "base/leisureItems.html", data)

    else:
        product = request.POST.get("product")
        remove = request.POST.get("remove")
        cart = request.session.get("cart")
        if cart:
            quantity = cart.get(product)
            if quantity:
                if remove:
                    if quantity == 1:
                        cart.pop(product)
                    else:
                        cart[product] = quantity - 1
                else:
                    cart[product] = quantity + 1
            else:
                cart[product] = 1
        else:
            cart = {}
            cart[product] = 1

        request.session["cart"] = cart

        return redirect("leisureItems")


def assamiveProducts(request):
    if request.method == "GET":
        cart = request.session.get("cart")
        if not cart:
            request.session["cart"] = {}
        products = Product.get_all_products()[109:116]
        data = {}
        data["products"] = products
        return render(request, "base/assamiveProducts.html", data)

    else:
        product = request.POST.get("product")
        remove = request.POST.get("remove")
        cart = request.session.get("cart")
        if cart:
            quantity = cart.get(product)
            if quantity:
                if remove:
                    if quantity == 1:
                        cart.pop(product)
                    else:
                        cart[product] = quantity - 1
                else:
                    cart[product] = quantity + 1
            else:
                cart[product] = 1
        else:
            cart = {}
            cart[product] = 1

        request.session["cart"] = cart

        return redirect("assamiveProducts")


def checkPhotos(request):
    return render(request, "base/checkPhotos.html")


def about(request):
    return render(request, "base/about.html")


@auth_middleware
def comment(request):
    form = commentForm()
    if request.method == "POST":
        form = commentForm(request.POST)
        if form.is_valid():
            form.save()
            #         comment = form.save(commit=False)
            #         comment.customer = request.customer
            #         comment.save()
            return redirect("comment")  # Redirect to a page displaying all comments
    # else:
    #     form = commentForm()

    # comments = Comment.objects.all()
    # context = {"comments": comments, "form": form}

    context = {"form": form}

    return render(request, "base/comment.html", context)


def validatedCustomer(customer):
    error_message = None

    if not customer.first_name:
        error_message = "First name required !!"

    elif len(customer.first_name) < 4:
        error_message = "First name must be 4 char long or more "

    elif customer.isExists():
        error_message = "Email Address already exists"

    return error_message


def registerUser(request):
    postData = request.POST
    first_name = postData.get("firstname")
    last_name = postData.get("lastname")
    # phone = postData.get("phone")
    email = postData.get("email")
    password = postData.get("password")
    # print(first_name, last_name, phone, email, password)

    # validation

    error_message = None

    customer = Customer(
        first_name=first_name,
        last_name=last_name,
        # phone=phone,
        email=email,
        password=password,
    )
    error_message = validatedCustomer(customer)

    # saving
    if not error_message:
        # print(first_name, last_name, email, password)
        customer.password = make_password(customer.password)
        customer.register()

        return render(request, "base/login.html", {"error": error_message})


def signIn(request):
    if request.method == "GET":
        return render(request, "base/signIn.html")

    else:
        return registerUser(request)

        # return redirect("home")

        # return HttpResponse("Sign in success")

        # return HttpResponse(request.POST.get("email"))


# class login(View):
#     def get(self, request):
#         return render(request, "base/login.html")

#     def post(self, request):
#         email = request.POST.get("email")
#         password = request.POST.get("password")
#         customer = Customer.get_customer_by_email(email)
#         error_message = None
#         if customer:
#             flag = check_password(password, customer.password)
#             if flag:
#                 return redirect("homepage")
#             else:
#                 error_message = "Email or Password invalid"

#         else:
#             error_message = "Email or Password invalid"

#         return render(request, "base/login.html", {"error": error_message})


def login(request):
    return_url = None

    if request.method == "GET":
        return_url = request.GET.get("return_url")
        return render(request, "base/login.html")
    else:
        email = request.POST.get("email")
        password = request.POST.get("password")
        customer = Customer.get_customer_by_email(email)
        error_message = None
        if customer:
            flag = check_password(password, customer.password)
            if flag:
                # request.session["customer_id"] = customer.id
                # request.session["email"] = customer.email
                request.session["customer"] = customer.id

                # return redirect("home")

                if return_url:
                    return HttpResponseRedirect(return_url)
                else:
                    return_url = None
                    return redirect("home")

            else:
                error_message = "Email or Password invalid"

        else:
            error_message = "Email or Password invalid"

        return render(request, "base/login.html", {"error": error_message})


def logout(request):
    request.session.clear()
    return redirect("login")


@auth_middleware
def cart(request):
    if request.method == "GET":
        cart = request.session.get(
            "cart", {}
        )  # Provide a default value if "cart" is not present
        ids = list(cart.keys())
        products = Product.get_products_by_id(ids)
        return render(request, "base/cart.html", {"products": products})
    else:
        # Handle other HTTP methods if needed
        pass


@auth_middleware
def checkout(request):
    if request.method == "POST":
        customer = request.session.get("customer")
        cart = request.session.get("cart")
        products = Product.get_products_by_id(list(cart.keys()))
        orders = Order.get_orders_by_customer(customer)

        for product in products:
            order = Order(
                customer=Customer(id=customer),
                product=product,
                price=product.price,
                quantity=cart.get(str(product.id)),
            )

            order.placeOrder()
            # order.save()

        request.session["cart"] = {}

        # return redirect("cart")
        return render(request, "base/checkout.html", {"orders": orders})

    else:
        pass


def order(request):
    if request.method == "GET":
        return render(request, "base/orders.html")
    else:
        pass


# def cart(request):
#     if request.method == "GET":
#         ids = list(request.session.get("cart").keys())
#         products = Product.get_products_by_id(ids)
#         return render(request, "base/cart.html", {"products": products})
#         # for x in ids:
#         #     product = Product.get_products_by_id(x)
#         #     return render(request, "cart.html", {"product": product})
#     else:
#         pass


# def deleteOrder(request):
#     if request.method == "POST":
#         if "order_id" in request.POST:
#             order_id = request.POST["order_id"]
#             current_user = request.customer
#             current_order = Order.objects.get(id=order_id)
#             current_order.delete()
#             return redirect("order")


#
# def cancel_order(request, order_id):
#     if request.method == "POST":
#         # Fetch the order and check if it belongs to the logged-in customer
#         order = Order.objects.get(id=order_id)
#         if order.customer == request.session.get("customer"):
#             # You might want to add additional checks or logic here based on your requirements
#             order.delete()  # Delete the order
#     return redirect("checkout")


# @auth_middleware
# def cancel_order(request, pk):
#     order = Order.objects.get(id=pk)
#     if request.method == "POST":
#         if order.customer == request.session.get("customer"):
#             # You might want to add additional checks or logic here based on your requirements
#             order.delete()  # Delete the order
#     return redirect("checkout")

from django import template


register = template.Library()


@register.filter(name="is_in_cart")
def is_in_cart(product, cart):
    keys = cart.keys()
    for id in keys:
        if int_or_0(id) == product.id:
            return True
    return False


def int_or_0(value):
    try:
        return int(value)
    except:
        return 0


# def is_in_cart(product, cart):
# keys = cart.keys()


# def is_in_cart(product, cart):
#     keys = cart.keys()
#     for id in keys:
#         if int(id) == product.id:
#             return True
#     return False


@register.filter(name="cart_quantity")
def cart_quantity(product, cart):
    keys = cart.keys()
    for id in keys:
        if int_or_0(id) == product.id:
            return cart.get(id)
    return False


@register.filter(name="price_total")
def price_total(product, cart):
    return product.price * cart_quantity(product, cart)


@register.filter(name="total_cart_price")
def total_cart_price(products, cart):
    sum = 0
    for p in products:
        sum += price_total(p, cart)

    return sum


@register.filter(name="multiply")
def multiply(number, number1):
    return number * number1


# def int_or_0(value):
#     try:
#         return int(value)
#     except:
#         return 0


# @register.filter(name="cart_quantity")
# def cart_quantity(product, cart):
#     product_id = str(product.id)

#     if product_id in cart:
#         return cart[product_id]

#     return 0

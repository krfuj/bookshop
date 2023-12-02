from basket.basket import Basket
from django.http.response import JsonResponse
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.template.loader import render_to_string
from .models import Order, OrderItem
from decimal import Decimal
from django.shortcuts import render

import os


# def add(request):
#     basket = Basket(request)
#     if request.POST.get("action") == "post":

#         order_key = request.POST.get("order_key")
#         user_id = request.user.id
#         baskettotal = basket.get_total_price()

#         # Check if order exists
#         if Order.objects.filter(order_key=order_key).exists():
#             pass
#         else:
#             order = Order.objects.create(
#                 user_id=user_id,
#                 full_name="name",
#                 address1="add1",
#                 address2="add2",
#                 total_paid=baskettotal,
#                 order_key=order_key,
#             )
#             order_id = order.pk

#             for item in basket:
#                 OrderItem.objects.create(
#                     order_id=order_id,
#                     product=item["product"],
#                     price=item["price"],
#                     quantity=item["qty"],
#                 )

#         # response = JsonResponse({"success": "Return something"})
#         # return response
#         return HttpResponseRedirect('/order_placed.html/')
#     return HttpResponseRedirect('/order_placed.html/')


from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from decimal import Decimal
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.base import TemplateView



from django.shortcuts import get_object_or_404



#############################good#################################################


# def add(request):
#     basket = Basket(request)
#     if request.method == 'POST':
#         order_key = request.POST.get("order_key")
#         user_id = request.user.id

#         try:
#             total_paid_string = basket.get_total_price()
#             total_paid_string = 11
#             total_paid = Decimal(total_paid_string)
#         except decimal.InvalidOperation:
#             error_message = "Invalid total_paid value: {}".format(total_paid_string)
#             return redirect('/order_error.html?error={}'.format(error_message))

#         existing_order = Order.objects.filter(order_key=order_key).first()
#         if existing_order:
#             existing_order.total_paid = total_paid
#             existing_order.save()

#             # Get or create an OrderItem object with the ID of 1
#             product, created = OrderItem.objects.get_or_create(pk=1)

#             # Set the price field for the OrderItem object before trying to save it
#             product.price = product.product.price

#             order_item = OrderItem.objects.filter(order=existing_order, product=product).first()

#             if order_item:
#                 order_item.quantity += 1
#                 order_item.save()
#             else:
#                 OrderItem.objects.create(order=existing_order, product=product, price=product.price, quantity=1)

#             return redirect('/order_placed.html/')
#         else:
#             order = Order.objects.create(user_id=user_id, full_name="name", address1="add1", address2="add2", total_paid=total_paid, order_key=order_key)
#             order_id = order.pk

#             # Get or create an OrderItem object with the ID of 1
#             product, created = OrderItem.objects.get_or_create(pk=1)

#             # Set the price field for the OrderItem object before trying to save it
#             product.price = product.product.price

#             OrderItem.objects.create(order_id=order_id, product=product, price=product.price, quantity=1)

#             return redirect('/order_placed.html/')
#     else:
#         return render(request, 'add_order.html', {'basket': basket})
##################################END#######################################################
from django.shortcuts import render


# def add(request):
#     basket = Basket(request)

#     if request.method == 'POST':
#         order_key = request.POST.get("order_key")
#         user_id = request.user.id

#         try:
#             # total_paid_string = basket.get_total_price()
#             total_paid_string = 11
#             total_paid = Decimal(total_paid_string)
#         except decimal.InvalidOperation:
#             error_message = "Invalid total_paid value: {}".format(total_paid_string)
#             return redirect('/order_error.html?error={}'.format(error_message))

#         existing_order = Order.objects.filter(order_key=order_key).first()

#         if existing_order:
#             # Order already exists, no need to create OrderItem object
#             existing_order.total_paid = total_paid
#             existing_order.save()
#         else:
#             # Order does not exist, create OrderItem object
#             order = Order.objects.create(user_id=user_id, full_name="name", address1="add1", address2="add2", total_paid=total_paid, order_key=order_key)
#             order_id = order.pk

#             # Get or create an OrderItem object with the ID of 1
#             product, created = OrderItem.objects.get_or_create(pk=1)

#             # Explicitly set the price field for the OrderItem object before saving
#             product.price = product.product.price
#             product.save()

#         return render(request, 'order_placed.html', {})
#     else:
#         return render(request, 'order_placed.html', {})


###############################################second############################

def add(request):
    basket = Basket(request)

    if request.method == 'POST':
        order_key = request.POST.get("order_key")
        user_id = request.user.id

        try:
            total_paid_string = 10
            total_paid = Decimal(total_paid_string)
        except decimal.InvalidOperation:
            error_message = "Invalid total_paid value: {}".format(total_paid_string)
            # return redirect('/order_error.html?error={}'.format(error_message))
            return render(request, 'order_placed.html', {})

        existing_order = Order.objects.filter(order_key=order_key).first()

        if existing_order:
            # Order already exists, no need to create OrderItem object
            existing_order.total_paid = total_paid
            existing_order.save()
        else:
            # Order does not exist, create OrderItem object
            # order = Order.objects.create(user_id=user_id, full_name="name", address1="add1", address2="add2", total_paid=total_paid, order_key=order_key)
            # order_id = order.pk

            # Hardcode price for testing
            product_price = 10.00  # Replace with actual price retrieval logic for production

            # Get or create an OrderItem object with the ID of 1
            # product, created = OrderItem.objects.get_or_create(pk=1)

            # Set the price field for the OrderItem object
            # product.price = product_price
            # product.save()

        return render(request, 'order_placed.html', {})
    else:
        return render(request, 'order_placed.html', {})




# def payment_confirmation(data):
#     pass
#     return render(request, 'order_placed.html', {})
def payment_confirmation(request):
    # Your code here
    return render(request, 'order_placed.html', {})



def user_orders(request):
    user_id = request.user.id
    orders = Order.objects.filter(user_id=user_id).filter(is_delivered=True)
    return orders

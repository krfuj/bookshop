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



##################################END#######################################################
from django.shortcuts import render



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
           
            # Hardcode price for testing
            product_price = 100.00  # 

        return render(request, 'order_placed.html', {})
    else:
        return render(request, 'order_placed.html', {})




# def payment_confirmation(data):
#     pass
#     return render(request, 'order_placed.html', {})
def payment_confirmation(request):
    pass
    return render(request, 'order_placed.html', {})



def user_orders(request):
    user_id = request.user.id
    orders = Order.objects.filter(user_id=user_id).filter(is_delivered=True)
    return orders

import json

import stripe
from basket.basket import Basket
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.base import TemplateView
from orders.views import payment_confirmation



def order_placed(request):
    basket = Basket(request)
    basket.clear()
    return render(request, "order_placed.html")


class Error(TemplateView):
    template_name = "error.html"


@login_required
def BasketView(request):

    basket = Basket(request)
    total = str(basket.get_total_price())
    total = total.replace(".", "")
    total = int(total)

    stripe.api_key = "sk_test_51OIaIsH7l1aq9jNsUyq13XQj9s4IcqciyR8JoLXwhQqkwZn6n7X7HhOAxwyh6FTIsuKTjoQfPSW9jk1bgJpprXdE00ubqz25wf"
    intent = stripe.PaymentIntent.create(
        amount=total, currency="gbp", metadata={"userid": request.user.id}
    )

    return render(request, "home.html", {"client_secret": intent.client_secret})


@csrf_exempt
def stripe_webhook(request):
    payload = request.body
    event = None

    try:
        event = stripe.Event.construct_from(json.loads(payload), stripe.api_key)
    except ValueError as e:
        print(e)
        return HttpResponse(status=400)

    # Handle the event
    if event.type == "payment_intent.succeeded":
        payment_confirmation(event.data.object.client_secret)

    else:
        print("Unhandled event type {}".format(event.type))

    return HttpResponse(status=200)


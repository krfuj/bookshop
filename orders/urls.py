from django.urls import path

from . import views

# urlpatterns = [path("add/", views.add, name="add")]


from django.urls import path
from . import views

urlpatterns = [
    path("add/", views.add, name="add"),
    path("payment_confirmation/", views.payment_confirmation, name="payment_confirmation"),
    # Add more paths here as needed
]



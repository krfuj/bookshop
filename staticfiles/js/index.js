var stripe = Stripe('pk_test_51OIaIsH7l1aq9jNsyntCDVvlwGOWQyqsS3oTGRNDKn5pqPJmB0aspen8TOARFmP2D7xQDhIMmeEhib1MnKCiv9Ei0077YJZwH0');

var elem = document.getElementById('submit');
clientsecret = elem.getAttribute('data-secret');

// Set up Stripe.js and Elements to use in checkout form
var elements = stripe.elements();
var style = {
  base: {
    color: "#000",
    lineHeight: '2.4',
    fontSize: '16px'
  }
};

var card = elements.create("card", { style: style });
card.mount("#card-element");

card.on('change', function (event) {
  var displayError = document.getElementById('card-errors');
  if (event.error) {
    displayError.textContent = event.error.message;
    $('#card-errors').addClass('alert alert-info');
  } else {
    displayError.textContent = '';
    $('#card-errors').removeClass('alert alert-info');
  }
});

var form = document.getElementById('payment-form');

form.addEventListener('submit', function (ev) {
  ev.preventDefault();

  var custName = document.getElementById("custName").value;
  var custAdd = document.getElementById("custAdd").value;
  var custAdd2 = document.getElementById("custAdd2").value;
  var postCode = document.getElementById("postCode").value;

  $.ajax({
    type: "POST",
    url: 'http://127.0.0.1:8000/orders/add/',
    data: {
      order_key: clientsecret,
      csrfmiddlewaretoken: CSRF_TOKEN,
      action: "post",
    },
    success: function (json) {
      console.log(json.success);

      stripe.confirmCardPayment(clientsecret, {
        payment_method: {
          card: card,
          billing_details: {
            address: {
              line1: custAdd,
              line2: custAdd2
            },
            name: custName
          }
        }
      }).then(function (result) {
        if (result.error) {
          console.log('payment error');
          console.log(result.error.message);

          // Render error message to the order_placed.html template
          $.get('/payment/templates/order_placed.html', function (template) {
            $('#payment-form').html(template);
            $('#payment-form').prepend('<div class="alert alert-danger">Payment failed: ' + result.error.message + '</div>');
          });
        } else {
          if (result.paymentIntent.status === 'succeeded') {
            console.log('payment processed');

            // Redirect to order_placed.html template upon successful payment
            window.location.replace("/payment/templates/order_placed.html");
          }
        }
      });
    },
    error: function (xhr, errmsg, err) {
      console.error('AJAX error:', errmsg, err);
    }
  });
});

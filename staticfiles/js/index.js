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
    var displayError = document.getElementById('card-errors')
    if (event.error) {
        displayError.textContent = event.error.message;
        $('#card-errors').addClass('alert alert-info');
    } else {
        displayError.textContent = '';
        $('#card-errors').removeClass('alert alert-info');
    }
});

var form = document.getElementById('payment-form');

async function confirmPaymentIntent() {
  const paymentIntentId = 'pi_3OIpEGH7l1aq9jNs0tCqrpTN';
  console.log(paymentIntent)

  try {
    // Check if the payment intent exists before attempting to confirm it
    const paymentIntent = await stripe.paymentIntents.retrieve(paymentIntentId);

    if (!paymentIntent) {
      // Payment intent not found, redirect to error page
      window.location.href = '/error.html';
      return;
    }

    // Payment intent exists, attempt to confirm it
    const confirmedPaymentIntent = await stripe.paymentIntents.confirm(paymentIntentId);

    // Handle successful payment intent confirmation
  } catch (error) {
    // Handle other errors
    console.error(error);
  }
}


form.addEventListener('submit', function (ev) {
    ev.preventDefault();

    var custName = document.getElementById("custName").value;
    var custAdd = document.getElementById("custAdd").value;
    var custAdd2 = document.getElementById("custAdd2").value;
    var postCode = document.getElementById("postCode").value;

    
    

      


//     $.ajax({
//         type: "POST",
//         url: 'http://127.0.0.1:8000/payment/templates/order_placed.html',
//         // http://127.0.0.1:5500/payment/templates/order_placed.html
//         data: {
//             order_key: clientsecret,
//             csrfmiddlewaretoken: CSRF_TOKEN,
//             action: "post",
//         },
//         success: function (json) {
//             console.log(json.success)

//             stripe.confirmCardPayment(clientsecret, {
//                 payment_method: {
//                     card: card,
//                     billing_details: {
//                         address: {
//                             line1: custAdd,
//                             line2: custAdd2
//                         },
//                         name: custName
//                     },
//                 }
//             }).then(function (result) {
//                 if (result.error) {
//                     console.log('payment error')
//                     console.log(result.error.message);
//                 } else {
//                     if (result.paymentIntent.status === 'succeeded') {
//                         console.log('payment processed')
//                         // There's a risk of the customer closing the window before callback
//                         // execution. Set up a webhook or plugin to listen for the
//                         // payment_intent.succeeded event that handles any business critical
//                         // post-payment actions.
//                         window.location.replace("http://127.0.0.1:5500/orderplaced/");
//                     }
//                 }
//             });

//         },
//         error: function (xhr, errmsg, err) { },
//     });

 });
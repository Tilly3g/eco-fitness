from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from bag.contexts import bag_contents
from django.conf import settings

from .forms import PaymentForm
import stripe


def payment(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "Looks like you haven't added any sessions to your bag")
        return redirect(reverse('bookings'))

    bag = bag_contents(request)
    total = bag['total']
    stripe_total = round(total * 100)
    stripe.api_key = stripe_secret_key
    intent = stripe.PaymentIntent.create(
        amount=stripe_total,
        currency=settings.STRIPE_CURRENCY,
    )

    payment_form = PaymentForm()

    if not stripe_public_key:
        messages.warning(request, 'Stripe public key is missing. \
            Did you forget to set it in your environment?')

    template = 'payments/payment.html'
    context = {
        'payment_form': payment_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)


from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.conf import settings
from django.views.decorators.http import require_POST

from .forms import PaymentForm
from bag.contexts import bag_contents
from .models import Payment, OrderLineItem
from bookings.models import Session

import stripe
import json


@require_POST
def cache_payment_data(request):
    try:
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(pid, metadata={
            'bag': json.dumps(request.session.get('bag', {})),
            'save_info': request.POST.get('save_info'),
            'username': request.user,
        })
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, 'Sorry, your payment cannot be \
            processed right now. Please try again later.')
        return HttpResponse(content=e, status=400)


def payment(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        bag = request.session.get('bag', {})

        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'country': request.POST['country'],
            'street_address1': request.POST['street_address1'],
            'street_address2': request.POST['street_address2'],
            'town_or_city': request.POST['town_or_city'],
            'postcode': request.POST['postcode'],
            'county': request.POST['county'],
        }
        payment_form = PaymentForm(form_data)
        if payment_form.is_valid():
            order = payment_form.save(commit=False)
            pid = request.POST.get('client_secret').split('_secret')[0]
            order.stripe_pid = pid
            order.original_bag = json.dumps(bag)
            order.save()
            for booking_id, booking_data in bag.items():
                try:
                    booking = Session.objects.get(id=booking_id)
                    if isinstance(booking_data, int):
                        order_line_item = OrderLineItem(
                            order=order,
                            booking=booking,
                            quantity=booking_data,
                        )
                        order_line_item.save()
                    else:
                        for quantity in booking_data.items():
                            order_line_item = OrderLineItem(
                                order=order,
                                booking=booking,
                                quantity=quantity,
                            )
                            order_line_item.save()
                except Session.DoesNotExist:
                    messages.error(request, (
                        "One of the session types wasn't found in our database. "
                        "Contact us for assistance!")
                    )
                    order.delete()
                    return redirect(reverse('view_bag'))

            request.session['save_info'] = 'save-info' in request.POST
            return redirect(reverse('payment_success', args=[order.order_number]))
        else:
            messages.error(request, 'There was an error with your payment. \
                Please check the information you have entered.')
    else:
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


def payment_success(request, order_number):
    """
    Successful payments
    """
    save_info = request.session.get('save_info')
    booking = get_object_or_404(Payment, order_number=order_number)
    messages.success(request, f'Booking successfully processed! \
        Your order number is {order_number}. A confirmation \
        email will be sent to {booking.email} and your Expert will be in touch shortly by phone or email to book in a time and date.')

    if 'bag' in request.session:
        del request.session['bag']

    template = 'payments/payment_success.html'
    context = {
        'booking': booking,
    }

    return render(request, template, context)

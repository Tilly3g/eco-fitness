from django.http import HttpResponse

from .models import Payment, OrderLineItem
from bookings.models import Session

import json
import time

class StripeWH_Handler:
    """Handle Stripe webhooks"""

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """
        Handle a generic/unknown/unexpected webhook event
        """
        return HttpResponse(
            content=f'Webhook not handled: {event["type"]}',
            status=200)

    def handle_payment_intent_succeeded(self, event):
        """
        Handle the payment_intent.succeeded webhook from Stripe
        """
        intent = event.data.object
        pid = intent.id
        bag = intent.metadata.bag
        save_info = intent.metadata.save_info

        billing_details = intent.charges.data[0].billing_details
        total = round(intent.charges.data[0].amount / 100, 2)

        # Clean data in the billing details
        for field, value in billing_details.address.items():
            if value == "":
                billing_details.address[field] = None

        payment_exists = False
        attempt = 1
        while attempt <= 5:
            try:
                payment = Payment.objects.get(
                    full_name__iexact=billing_details.name,
                    email__iexact=billing_details.email,
                    phone_number__iexact=billing_details.phone,
                    country__iexact=billing_details.address.country,
                    street_address1__iexact=billing_details.address.line1,
                    street_address2__iexact=billing_details.address.line2,
                    town_or_city__iexact=billing_details.address.city,
                    county__iexact=billing_details.address.state,
                    postcode__iexact=billing_details.address.postal_code,
                    total=total,
                    original_bag=bag,
                    stripe_pid=pid,
                )
                payment_exists = True
                break
            except Payment.DoesNotExist:
                attempt += 1
                time.sleep(1)
        if payment_exists:
            return HttpResponse(
                content=f'Webhook received: {event["type"]} | SUCCESS: Verified order already in database',
                status=200)
        else:
            payment = None
            try:
                payment = Payment.objects.create(
                    full_name=billing_details.name,
                    email=billing_details.email,
                    phone_number=billing_details.phone,
                    country=billing_details.address.country,
                    postcode=billing_details.address.postal_code,
                    town_or_city=billing_details.address.city,
                    street_address1=billing_details.address.line1,
                    street_address2=billing_details.address.line2,
                    county=billing_details.address.state,
                    original_bag=bag,
                    stripe_pid=pid,
                )
                for booking_id, booking_data in json.loads(bag).items():
                    booking = Session.objects.get(id=booking_id)
                    if isinstance(booking_data, int):
                        order_line_item = OrderLineItem(
                            payment=payment,
                            booking=booking,
                            quantity=booking_data,
                        )
                        order_line_item.save()
                    else:
                        for quantity in booking_data.items():
                            order_line_item = OrderLineItem(
                                payment=payment,
                                booking=booking,
                                quantity=quantity,
                            )
                            order_line_item.save()
            except Exception as e:
                if payment:
                    payment.delete()
                return HttpResponse(
                    content=f'Webhook received: {event["type"]} | ERROR: {e}',
                    status=500)
        return HttpResponse(
            content=f'Webhook received: {event["type"]} | SUCCESS: Created order in webhook',
            status=200)

    def handle_payment_intent_payment_failed(self, event):
        """
        Handle the payment_intent.payment_failed webhook from Stripe
        """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)

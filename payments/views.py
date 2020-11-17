from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import PaymentForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "Looks like you haven't added any sessions to your bag")
        return redirect(reverse('bookings'))

    payment_form = PaymentForm()
    template = 'payments/payment.html'
    context = {
        'payment_form': payment_form,
    }

    return render(request, template, context)

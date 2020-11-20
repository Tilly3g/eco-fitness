from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import PaymentForm


def payment(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "Looks like you haven't added any sessions to your bag")
        return redirect(reverse('bookings'))

    payment_form = PaymentForm()
    template = 'payments/payment.html'
    context = {
        'payment_form': payment_form,
        'stripe_public_key': 'pk_test_51HQUWIF2o3SAzBbaqfxCWJ6WIxzMwjPDqkOCl70dHiLa20draxmnfL488x2agn0Awp3t7zOpiYF2opi5Ywg9Mmnq00TAv8m7HF',
        'stripe_secret_key': 'STRIPE_SECRET_KEY',
    }

    return render(request, template, context)

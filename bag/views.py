from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages
from bookings.models import Session

# Create your views here.


def view_bag(request):
    """ A view that renders the bag contents page """

    return render(request, 'bag/bag.html')


def add_to_bag(request, booking_id):
    """ Add amount of the specified food to the diary """

    booking = get_object_or_404(Session, pk=booking_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url' or '/')
    bag = request.session.get('bag', {})

    if booking_id in list(bag.keys()):
        bag[booking_id] += quantity
        messages.success(request, f'Updated {booking.name} session quantity to {bag[booking_id]}')
    else:
        bag[booking_id] = quantity
        messages.success(request, f'Added {booking.name} session to your bag')

    request.session['bag'] = bag
    return redirect(redirect_url or '/')


def adjust_bag(request, booking_id):
    """Adjust the quantity of the session to a new quantity"""

    booking = get_object_or_404(Session, pk=booking_id)
    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('bag', {})

    if quantity > 0:
        bag[booking_id] = quantity
        messages.success(request, f'Updated {booking.name} session quantity to {bag[booking_id]}')
    else:
        bag.pop(booking_id)
        messages.success(request, f'Removed {booking.name} session from your bag')

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def remove_from_bag(request, booking_id):
    """Remove the session from the shopping bag completely"""

    try:
        booking = get_object_or_404(Session, pk=booking_id)
        bag = request.session.get('bag', {})

        bag.pop(booking_id)
        messages.success(request, f'Removed {booking.name} session from your bag')

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)

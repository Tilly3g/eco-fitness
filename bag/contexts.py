from django.shortcuts import get_object_or_404
from bookings.models import Session


def bag_contents(request):

    bag_bookings = []
    total = 0
    booking_count = 0
    bag = request.session.get('bag', {})

    for booking_id, booking_data in bag.items():
        if isinstance(booking_data, int):
            booking = get_object_or_404(Session, pk=booking_id)
            total += booking_data * booking.price
            booking_count += booking_data
            bag_bookings.append({
                'booking_id': booking_id,
                'quantity': booking_data,
                'booking': booking,
            })
        else:
            booking = get_object_or_404(Session, pk=booking_id)
            for quantity in booking_data[booking_id].items():
                total += quantity * booking.price
                booking_count += quantity
                bag_bookings.append({
                    'booking_id': booking_id,
                    'quantity': quantity,
                    'booking': booking,
                })

    context = {
        'bag_bookings': bag_bookings,
        'total': total,
        'booking_count': booking_count,
    }

    return context

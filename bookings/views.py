from django.shortcuts import render
from .models import Session

# Create your views here.


def all_bookings(request):

    bookings = Session.objects.all()

    context = {
        'bookings': bookings,
    }

    return render(request, 'bookings/bookings.html', context)

from django.shortcuts import render, redirect, reverse, HttpResponse

# Create your views here.

def view_bag(request):
    """ A view that renders the bag contents page """

    return render(request, 'bag/bag.html')


def add_to_bag(request, booking_id):
    """ Add amount of the specified food to the diary """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if booking_id in list(bag.keys()):
        bag[booking_id] += quantity
    else:
        bag[booking_id] = quantity

    request.session['bag'] = bag
    return redirect(redirect_url)


def adjust_bag(request, booking_id):
    """Adjust the quantity of the session to a new quantity"""

    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('bag', {})

    if quantity > 0:
        bag[booking_id] = quantity
    else:
        bag.pop(booking_id)

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def remove_from_bag(request, booking_id):
    """Remove the session from the shopping bag completely"""

    try:
        bag = request.session.get('bag', {})

        bag.pop(booking_id)

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        return HttpResponse(status=500)

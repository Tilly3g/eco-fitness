from django.shortcuts import render, redirect

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

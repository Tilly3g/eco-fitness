from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Session
from .forms import SessionUpdate


# Create your views here.


def all_bookings(request):

    bookings = Session.objects.all()

    context = {
        'bookings': bookings,
    }

    return render(request, 'bookings/bookings.html', context)


@login_required
def add_session(request):
    """ Add a session type to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Opps, only administrators can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = SessionUpdate(request.POST, request.FILES)
        if form.is_valid():
            session = form.save()
            messages.success(request, f'Successfully added {session.name} session with {session.Expert}!')
            return redirect(reverse('bookings'))
        else:
            messages.error(request, 'Error adding session type. Please ensure the form is valid.')
    else:
        form = SessionUpdate()

    template = 'bookings/add_session.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


def session_info(request, session_id):
    """ A view to show session info for editing """

    session = get_object_or_404(Session, pk=session_id)

    context = {
        'booking': session,
    }

    return render(request, 'bookings/booking_view.html', context)


@login_required
def edit_session(request, session_id):
    """ Edit an existing session type """
    if not request.user.is_superuser:
        messages.error(request, 'Oops, only administrators can do that.')
        return redirect(reverse('home'))

    session = get_object_or_404(Session, pk=session_id)
    if request.method == 'POST':
        form = SessionUpdate(request.POST, instance=session)
        if form.is_valid():
            form.save()
            messages.success(request, f'Successfully updated {session.name} session with {session.Expert}!')
            return redirect('bookings')
        else:
            messages.error(request, 'Error updating session type. Please ensure the form is valid.')
    else:
        form = SessionUpdate(instance=session)
        messages.info(request, f'You are editing {session.name} session with {session.Expert}.')

    template = 'bookings/edit_session.html'
    context = {
        'form': form,
        'session': session,
    }

    return render(request, template, context)


@login_required
def delete_session(request, session_id):
    """ Delete session type from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Oops, only administrators can do that.')
        return redirect(reverse('home'))

    session = get_object_or_404(Session, pk=session_id)
    session.delete()
    messages.success(request, f'{session.name} session with {session.Expert} deleted!')
    return redirect(reverse('bookings'))

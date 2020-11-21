from django.shortcuts import render, get_object_or_404
from django.contrib import messages

from .models import UserProfile
from .forms import UserForm


def profile(request):
    """ Display profile. """

    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated your Profile')

    form = UserForm(instance=profile)
    payments = profile.payments.all()

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'payments': payments,
        'update_profile': True
    }

    return render(request, template, context)

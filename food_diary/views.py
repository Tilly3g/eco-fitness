from django.shortcuts import render, redirect

# Create your views here.

def view_diary(request):
    """ A view that renders the diary contents page """

    return render(request, 'food_diary/diary.html')


def add_to_diary(request, food_id):
    """ Add amount of the specified food to the diary """

    amount = int(request.POST.get('amount'))
    redirect_url = request.POST.get('redirect_url')
    diary = request.session.get('food_diary', {})

    if food_id in list(diary.keys()):
        diary[food_id] += amount
    else:
        diary[food_id] = amount

    request.session['food_diary'] = diary
    return redirect(redirect_url)

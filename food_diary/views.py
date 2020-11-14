from django.shortcuts import render

# Create your views here.

def view_diary(request):
    """ A view that renders the bag contents page """

    return render(request, 'food_diary/diary.html')

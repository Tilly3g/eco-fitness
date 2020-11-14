
def bag_contents(request):

    sessions = []
    total = 0
    session_count = 0

    context = {
        'sessions': sessions,
        'total': total,
        'session_count': session_count,
    }

    return context

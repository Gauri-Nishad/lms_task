from django.shortcuts import redirect
from django.contrib import messages

def admin_required(view_func):
    def wrapper(request, *args, **kwargs):
        if request.session.get('user_role') == 'admin':
            return view_func(request, *args, **kwargs)
        else:
            messages.error(request, "You are not authorized to access this page.")
            return redirect('app:home')
    return wrapper

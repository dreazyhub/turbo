from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

def custom_login_required(view_func):
    decorated_view_func = login_required(view_func)
    
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('AdminSide:login')  # Replace 'login' with the name of your login URL
        return decorated_view_func(request, *args, **kwargs)
    
    return wrapper
from django.shortcuts import redirect
from functools import wraps

def staff_required(view_func):
    """ Декоратор проверки текущего пользователя is_staff """
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if request.user.is_active and request.user.is_staff:
            return view_func(request, *args, **kwargs)
        
        # Если не админ — отправляем на главную
        return redirect('core:index') 
    return _wrapped_view

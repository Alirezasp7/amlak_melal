from functools import wraps

from django.core.exceptions import PermissionDenied


def is_consultant(user):
    if not user or not user.is_authenticated:
        return False

    return bool(getattr(user, "is_consultant", False))


def consultant_required(view_function):
    @wraps(view_function)

    def wrapper(request, *args, **kwargs):
        if not is_consultant(request.user):
            return PermissionDenied
        
        return view_function(request ,*args, **kwargs)
    return wrapper
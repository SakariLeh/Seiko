from flask import session, redirect, url_for

def check_auth_middleware(view_func):
    def wrapped_view(*args, **kwargs):
        if 'user_id' not in session:
            return redirect(url_for('auth.index'))
        return view_func(*args, **kwargs)

    wrapped_view.__name__ = view_func.__name__
    return wrapped_view
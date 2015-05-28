from django.shortcuts import redirect, render
from django.contrib import auth
from django.core.context_processors import csrf


def login(request):
    return_path = request.META.get('HTTP_REFERER', '/')
    args = {}
    args.update(csrf(request))
    if request.POST:
        email = request.POST.get('email', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=email, password=password)
        if user is not None:
            if user.is_active:
                auth.login(request, user)
                # TODO: if equal to login page path, redirect to index
                # return render(request, 'index.html', args)
                return redirect(return_path)
            else:
                return render(request, 'index.html', args)
        else:
            args['login_error'] = "Auth error"
            return render(request, 'login.html', args)
    else:
        return render(request, 'login.html', args)


def logout(request):
    return_path = request.META.get('HTTP_REFERER', '/')
    auth.logout(request)
    return redirect(return_path)
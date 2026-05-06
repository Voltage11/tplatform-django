from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm

def login_view(request):
    form = LoginForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                login(request, user)
                next_url = request.GET.get('next', 'core:index')
                return redirect(next_url)
            else:
                form.add_error(None, "Неверный логин или пароль")

    return render(request, 'user/login.html', {'form': form})

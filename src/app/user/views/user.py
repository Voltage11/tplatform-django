

from django.contrib.auth import login
# from app.user.forms import LoginForm
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect, render


def login_view(request):
    
    if request.user.is_authenticated:
            return redirect('core:index')
    
    if request.method == 'GET':                
        login_form = AuthenticationForm()        
                    
    if request.method == 'POST':
        login_form = AuthenticationForm(request, data=request.POST)
        if login_form.is_valid():
            user = login_form.get_user()
            login(request, user)
            return redirect('core:index')
        
    context = {
            'login_form': login_form,
        }    
        
    return render(request, 'user/login.html', context=context)
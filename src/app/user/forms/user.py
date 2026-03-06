from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(required=True, help_text='Введите логин', label='Логин')
    password = forms.CharField(required=True, help_text='Введите пароль', label='Пароль', widget=forms.PasswordInput)
    
    
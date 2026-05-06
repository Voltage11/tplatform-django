from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=255, 
        required=True, 
        help_text='Введите логин', 
        label='Логин',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'})
    )
    password = forms.CharField(
        required=True,
        label='Пароль',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': '********'})
    )

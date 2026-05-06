from django.urls import path
from app.user.views import login_view
from django.contrib.auth import views as auth_views


app_name = 'user'

urlpatterns = [
    path('login', login_view, name='login'),
    path('logout', auth_views.LogoutView.as_view(), name='logout'),
]


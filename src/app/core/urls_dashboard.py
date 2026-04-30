from django.urls import path
from app.core.views.index import index

app_name = 'core'

urlpatterns = [
    path('', index, name='index'),
]


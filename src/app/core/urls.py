from django.urls import path

from app.core.views.theme import get_theme_list, create_theme, update_theme

from .views import index_view

app_name = "core"

urlpatterns = [
    path("theme/list", get_theme_list, name="theme_list"),
    path("theme/create", create_theme, name="create_theme"),
    path("theme/<int:pk>", update_theme, name="update_theme"),
    path("", index_view, name="index"),
]

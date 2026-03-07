from typing import List
from django.urls import reverse, NoReverseMatch
import logging

logger = logging.getLogger(__name__)


class MainMenuItem:
    def __init__(
        self, title: str, path_name: str | None = None, url: str | None = None
    ):
        self.title = title
        self.path_name = path_name
        self.is_active = False

        # 1. Если передан path_name, пытаемся превратить его в URL
        if path_name:
            try:
                self.url = reverse(path_name)
            except NoReverseMatch:
                logger.error(f"Не верное имя url: {path_name}")
                self.url = url if url else "#"
        else:
            self.url = url if url else "#"

    def __repr__(self):
        return f"<MenuItem {self.title}: {self.url}>"


MENU_ADMIN = [
    MainMenuItem("Главная", "/admin/"),
    MainMenuItem("Темы для тестирования", "core:theme_list"),
    MainMenuItem("Организации", "/admin/settings/"),
    MainMenuItem("Отделы", "/admin/references/"),
    MainMenuItem("Сотрудники", "/admin/references/"),
]

MENU_USER = [
    MainMenuItem("Главная", "/"),
    MainMenuItem("Профиль", "/profile/"),
    MainMenuItem("Темы для тестирования", "/settings/"),
]


def main_menu(request):
    if not request.user.is_authenticated:
        return {}

    if request.user.is_superuser:
        return {
            "main_menu": MENU_ADMIN,
            "title": "Title",
            "local_title": "LocalTitle",
        }

    return {
        "main_menu": MENU_USER,
    }

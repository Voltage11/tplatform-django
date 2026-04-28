from typing import List


class MenuItem:
    def __init__(self, title, link: str):
        self.title = title
        self.link = link

    def __str__(self):
        return self.title


class Menu:
    Items: List[MenuItem]

    def __init__(self, items: List[MenuItem] | None):
        if items:
            self.Items = items

    def append(self, item: MenuItem):
        self.Items.append(item)

    def __str__(self):
        return str(self.Items)


MAIN_MENU = Menu(None)
MAIN_MENU.Items = [
    MenuItem('Главная', '#'),
    MenuItem('Вторая', '#'),
    MenuItem('Третья', '#'),
]

def main_menu(request) -> dict:

    return {
        'main_menu': MAIN_MENU,
        'is_admin' : request.user.is_authenticated and request.user.is_superuser,
        'is_staff' : request.user.is_authenticated and request.user.is_staff,
    }



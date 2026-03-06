from typing import List


class MainMenuItem:
    def __init__(self, title, url: str):
        self.title = title
        self.url = url
        self.is_active = False
    

MENU_ADMIN = [
    MainMenuItem('Главная', '/admin/'),
    MainMenuItem('Пользователи', '/admin/user/'),
    MainMenuItem('Настройки', '/admin/settings/'),
    MainMenuItem('Справочники', '/admin/references/'),
    MainMenuItem('Справочники', '/admin/references/'),
]

MENU_USER = [
    MainMenuItem('Главная', '/'),
    MainMenuItem('Профиль', '/profile/'),
    MainMenuItem('Настройки', '/settings/'),
]



def main_menu(request):
    if not request.user.is_authenticated:
        return {}
    
    if request.user.is_superuser:
        return {
            'main_menu': MENU_ADMIN,
            'title': 'Title',
            'local_title': 'LocalTitle',
        }
    
    return {
        'main_menu': MENU_USER,
    }
    

    
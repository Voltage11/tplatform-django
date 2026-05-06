from django.http import HttpRequest
from django.urls import reverse
from dataclasses import dataclass

@dataclass
class MenuItem:
    title: str
    url_name: str
    is_only_staff: bool = False
    is_only_admin: bool = False


MENU_CONFIG = [
    MenuItem('Главная', 'home'),
    MenuItem('Личный кабинет', 'profile'),
    MenuItem('Курсы', 'courses:list'),
    MenuItem('Аналитика', 'analytics:dashboard', is_only_staff=True),
    MenuItem('Админка', 'admin:index', is_only_admin=True),
]

def main_menu(request: HttpRequest) -> dict:
    is_admin = request.user.is_authenticated and request.user.is_superuser
    is_staff = request.user.is_authenticated and request.user.is_staff
    
    current_url_name = request.resolver_match.view_name if request.resolver_match else None
    
    visible_menu = []
    for item in MENU_CONFIG:
        # Проверка доступа
        if item.is_only_admin and not is_admin:
            continue
        if item.is_only_staff and not (is_staff or is_admin):
            continue
        
        # Определение активности
        is_active = (current_url_name == item.url_name)
        
        # Безопасная генерация ссылки
        try:
            link = reverse(item.url_name)
        except:
            link = "#" # На случай, если URL требует аргументов (pk)
        
        visible_menu.append({
            'title': item.title,
            'link': link,
            'is_active': is_active
        })
            
    return {
        'main_menu': visible_menu,
        'is_admin': is_admin,
        'is_staff': is_staff,
    }

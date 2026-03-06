from django import template


register = template.Library()

@register.simple_tag(takes_context=True)
def url_replace(context, **kwargs):
    """
    Берет текущие GET-параметры из запроса и заменяет/добавляет в них новые.
    """
    query = context['request'].GET.copy()
    for kwarg, value in kwargs.items():
        query[kwarg] = value
    return query.urlencode()

from datetime import datetime
from django import template

register = template.Library()

DATE_FORMATS = {
    'dmy': '%d %b %Y',
    'mdy': '%b %d %Y',
    'hms': '%H: %M: %S'
}


@register.simple_tag()
def current_time(format_string='dmy'):
    """ Регистрируем метод-тэг который будет добавлять текущее время """
    return datetime.utcnow().strftime(DATE_FORMATS[format_string])


@register.simple_tag(takes_context=True)
def url_replace(context, **kwargs):
    d = context['request'].GET.copy()
    for k, v in kwargs.items():
        d[k] = v
    return d.urlencode()

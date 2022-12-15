from django import template

register = template.Library()

@register.filter(name='cutown')
def cutown(value,arg):
    """
    cuts values of arg from string
    """
    return value.replace(arg,'')

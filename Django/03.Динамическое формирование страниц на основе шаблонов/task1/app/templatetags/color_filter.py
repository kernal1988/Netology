from django import template

register = template.Library()

@register.filter
def to_int(string):
    try:
        return float(string)
    except ValueError:
        return string
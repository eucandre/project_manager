from django import template

register = template.Library()


@register.filter
def to_uperstring(value):
    """All characters to upper"""
    return value.upper()


@register.filter
def to_translation(value, to):
    """Translate field label to especific alias"""
    return value.replace(value, to)

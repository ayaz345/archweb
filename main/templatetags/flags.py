from django import template
from django.utils.html import format_html

register = template.Library()


@register.simple_tag
def country_flag(country):
    if not country:
        return ''
    return format_html(
        f'<span class="fam-flag fam-flag-{str(country.code).lower()}" title="{str(country.name)}"></span> '
    )


# vim: set ts=4 sw=4 et:

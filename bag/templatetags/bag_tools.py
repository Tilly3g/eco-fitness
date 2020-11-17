from django import template


register = template.Library()


@register.filter(name='subtotal')
def csubtotal(price, quantity):
    return price * quantity

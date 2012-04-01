from django import template
register = template.Library()

def prefix(value, arg):
    return str(arg) + str(value)

register.filter("prefix", prefix)

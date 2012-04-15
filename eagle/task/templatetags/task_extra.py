from django import template
register = template.Library()

def dict_index(idx, arg):
    return arg[idx]

def prefix(value, arg):
    return str(arg) + str(value)

register.filter("prefix", prefix)
register.filter("dict_index", dict_index)

from django import template


register=template.Library()

def swap(value):
    return value.swapcase()

def count(value,user):
    user=input('Enter ch :')
    arg=0
    for i in value:
        if i.lower()==user:
            arg+=1
    return arg
register.filter('swap',swap)
register.filter('count',count)
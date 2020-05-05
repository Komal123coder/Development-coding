from django import template
register=template.Library()
#django.template.Library.filter()
@register.filter(name="cut")
def cut(value,arg):
    """
    this cuts the value of "arg" from the string
    """
    return value.replace(arg,'')

#register.filter('cut',cut)
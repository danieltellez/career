from django import template

from career.models import Career

register = template.Library()

@register.inclusion_tag('career/get_careers.html')
def get_careers(user):
    careers = Career.objects.filter(user=user)
    return {'careers': careers}

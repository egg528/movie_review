from django import template
from lists import models as list_models


register = template.Library()


@register.simple_tag(takes_context=True)
def on_favs(context, movie):
    user = context.request.user
    try:
        the_list = list_models.List.objects.get(user=user)
        if the_list is None:
            return the_list
        elif movie in the_list.movies.all():
            return the_list
        else:
            return None
    except list_models.List.DoesNotExist:
        return None

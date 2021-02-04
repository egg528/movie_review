from django import template
from discussions import models as discussion_models


register = template.Library()


@register.simple_tag(takes_context=True)
def on_favs(context, pk):
    user = context.request.user
    try:
        discussion = discussion_models.Discussion.objects.get(pk=pk)

        if user in discussion.participants.all():
            return discussion
        else:
            return None
    except discussion_models.Discussion.DoesNotExist:
        return None

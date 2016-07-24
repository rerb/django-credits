from django import template
from django.conf import settings

from ..models import Credit


register = template.Library()

DEFAULT_DJANGO_CREDITS_DELAY = 3000  # milliseconds
DEFAULT_DJANGO_CREDITS_LIGHTBOX_VERSION = "bootstrap"


@register.inclusion_tag("django_credits.html")
def django_credits():
    return {"credits": Credit.objects.all(),
            "django_credits_delay": getattr(
                settings,
                "DJANGO_CREDITS_DELAY",
                DEFAULT_DJANGO_CREDITS_DELAY),
            "lightbox_version": getattr(
                settings,
                "DJANGO_CREDITS_LIGHTBOX_VERSION",
                DEFAULT_DJANGO_CREDITS_LIGHTBOX_VERSION)}

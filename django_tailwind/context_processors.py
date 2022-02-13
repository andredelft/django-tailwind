from django.conf import settings


DEFAULT_CLASSES = {"prose": "prose"}


def tailwind_classes(request):

    classes = DEFAULT_CLASSES.copy()
    if hasattr(settings, "TAILWIND_CLASSES"):
        classes.update(settings.TAILWIND_CLASSES)

    return classes

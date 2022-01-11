from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model;
from django.conf import settings

class Command(BaseCommand):

    def handle(self, *args, **options):
        User = get_user_model()
        if not User.objects.filter(email=settings.DJANGO_EMAIL).exists():
            User.objects.create_superuser(
                username=settings.DJANGO_USER,
                email=settings.DJANGO_EMAIL,
                password=settings.DJANGO_PASSWORD)

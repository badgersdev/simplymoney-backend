from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
import os


class Command(BaseCommand):
    help = 'Creates default superuser if not exists'

    def handle(self, *args, **kwargs):
        User = get_user_model()
        email = os.getenv("DEFAULT_ADMIN_EMAIL", "admin@example.com")
        password = os.getenv("DEFAULT_ADMIN_PASSWORD", "admin123")

        if not User.objects.filter(email=email).exists():
            User.objects.create_superuser(
                email=email,
                password=password
            )
            self.stdout.write(self.style.SUCCESS(
                f"✅ Superuser '{email}' created"))
        else:
            self.stdout.write(self.style.WARNING(
                f"⚠️  Superuser '{email}' already exists"))

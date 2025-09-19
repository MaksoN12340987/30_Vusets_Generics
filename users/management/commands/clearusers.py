from typing import Any

from django.core.management.base import BaseCommand
from users.models import User


class Command(BaseCommand):
    def handle(self, *args: Any, **options: Any) -> str | None:
        users = User.objects.all()

        for user in users:
            user.delete()
            if user:
                self.stdout.write(
                    self.style.SUCCESS(f"Successfully delete: {user}")
                )
            else:
                self.stdout.write(self.style.WARNING("User already not exists"))

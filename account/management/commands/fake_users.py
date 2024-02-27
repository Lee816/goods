import random
from django.core.management.base import BaseCommand
from faker import Faker

from account.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        fake = Faker("ko_KR")
        for _ in range(20):
            name = fake.unique.name()
            email = fake.unique.free_email()
            phone = (
                "010-"
                + str(random.randint(1, 9999)).zfill(4)
                + "-"
                + str(random.randint(1, 9999)).zfill(4)
            )
            password = name + "1"

            new_user = User.objects.create(
                username=name, nickname=name, email=email, phone=phone
            )
            new_user.set_password(password)
            new_user.save()

        self.stdout.write(self.style.SUCCESS("Users created!"))

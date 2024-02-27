import os
import random
from django.core.management.base import BaseCommand
from django.shortcuts import get_object_or_404
from django.core.files import File

from account.models import User
from goods.models import Category, Entertainer, Goods, Design


class Command(BaseCommand):

    def handle(self, *args, **options):
        img_list = os.listdir("fake_img")

        for _ in range(10):
            design_list = [
                img_list[random.randint(0, len(img_list) - 1)] for _ in range(1, 3)
            ]
            category_list = [x.id for x in Category.objects.all()]
            entertainer_list = [x.id for x in Entertainer.objects.all()]
            user_list = [x.id for x in User.objects.all()]

            category = get_object_or_404(
                Category,
                id=category_list[random.randint(0, Category.objects.count() - 1)],
            )
            entertainer = get_object_or_404(
                Entertainer,
                id=entertainer_list[random.randint(0, Entertainer.objects.count() - 1)],
            )
            user = get_object_or_404(
                User, id=user_list[random.randint(0, User.objects.count() - 1)]
            )

            description = entertainer.name + "의 " + category.name + " 굿즈 입니다."

            goods = Goods.objects.create(
                category=category,
                entertainer=entertainer,
                creator=user,
                description=description,
            )

            for design in design_list:
                new_design = Design.objects.create(
                    goods=goods,
                    design=File(open(os.path.join("fake_img", design), "rb")),
                )
                new_design.save()

            goods.save()

        self.stdout.write(self.style.SUCCESS("Goods created!"))

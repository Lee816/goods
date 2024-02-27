from django.core.management.base import BaseCommand

from goods.models import Entertainer


class Command(BaseCommand):

    def handle(self, *args, **options):
        category = [
            "(여자)아이들",
            "아이브",
            "르세라핌",
            "뉴진스",
            "라이즈",
            "에스파",
            "태연",
            "정국",
            "임영웅",
            "투어스",
            "악뮤",
            "이무진",
            "세븐틴",
            "엔믹스",
            "비비",
            "QWER",
            "제니",
            "트와이스",
            "블랙핑크",
            "엑소",
            "잇지",
            "레드벨벳",
            "방탄소년단",
            "투모로우바이투모로우",
        ]

        for x in category:
            Entertainer.objects.create(name=x)

        self.stdout.write(self.style.SUCCESS("Entertainer created!"))

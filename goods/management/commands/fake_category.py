from django.core.management.base import BaseCommand

from goods.models import Category


class Command(BaseCommand):

    def handle(self, *args, **options):
        category = [
            "응원봉",
            "포토카드",
            "볼펜",
            "공책",
            "노트",
            "앨범",
            "다이어리",
            "머드컵",
            "술잔",
            "메모지",
            "연습장",
            "우산",
            "연필꽂이",
            "열쇠고리",
            "티셔츠",
            "스트랩",
            "타월",
            "쿠션",
            "담요",
            "퍼즐",
            "배지",
            "스티커",
            "아크릴스탠드",
            "포스트잇",
            "케이스",
        ]

        for x in category:
            Category.objects.create(name=x)

        self.stdout.write(self.style.SUCCESS("Category created!"))

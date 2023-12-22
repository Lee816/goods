from django.db import models
from django.contrib.auth.models import AbstractUser

from datetime import datetime


def user_image_path(instance, filename):
    return f"account/{datetime.today().year}.{datetime.today().month}/{datetime.today().day}/{instance.username}/{filename}"


class User(AbstractUser):
    # 사용 x
    first_name = None
    last_name = None

    # 사용 o
    username = models.CharField(max_length=25)
    nickname = models.CharField(max_length=25, unique=True)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, unique=True)
    introduce = models.TextField(blank=True)
    user_image = models.ImageField(default="user.jpg", upload_to=user_image_path)

    followings = models.ManyToManyField(
        "self", symmetrical=False, related_name="followers", blank=True
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # 로그인 id로 사용할 필드
    USERNAME_FIELD = "email"
    # 필수 작성 필드
    REQUIRED_FIELDS = ["username", "phone"]

    def __str__(self):
        return self.nickname

    @property
    def following_count(self):
        following_count = 0
        if self.followings.all():
            for _ in self.followings.all():
                following_count += 1

        return following_count

    @property
    def followers_count(self):
        followers_count = 0
        if self.followers.all():
            for _ in self.followers.all():
                followers_count += 1

        return followers_count

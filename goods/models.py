import os
from django.conf import settings
from django.db import models

from account.models import User


class Entertainer(models.Model):
    name = models.CharField(max_length=25, unique=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]
        indexes = [
            models.Index(fields=["name"]),
            models.Index(fields=["created_at"]),
            models.Index(fields=["updated_at"]),
        ]


class Category(models.Model):
    name = models.CharField(max_length=25, unique=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]
        indexes = [
            models.Index(fields=["name"]),
            models.Index(fields=["created_at"]),
            models.Index(fields=["updated_at"]),
        ]


class Goods(models.Model):
    entertainer = models.ForeignKey(
        Entertainer, on_delete=models.CASCADE, related_name="goods"
    )
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="goods"
    )
    creator = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="create_goods"
    )
    description = models.TextField(blank=True)
    likes = models.ManyToManyField(User, related_name="like_goods", blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"[{self.entertainer}] {self.creator} 굿즈"

    class Meta:
        ordering = ["-updated_at"]
        indexes = [
            models.Index(fields=["entertainer"]),
            models.Index(fields=["category"]),
            models.Index(fields=["creator"]),
            models.Index(fields=["created_at"]),
            models.Index(fields=["updated_at"]),
        ]

    @property
    def like_count(self):
        like_count = 0
        if self.likes.all():
            for _ in self.likes.all():
                like_count += 1

        return like_count

    @property
    def like_list(self):
        like_list = []
        for user in self.likes.all():
            like_list.append(user.nickname)

        return like_list

    def delete(self, *args, **kargs):
        if self.design.all():
            for design in self.design.all():
                os.remove(os.path.join(settings.MEDIA_ROOT, design.design.path))
        super(Goods, self).delete(*args, **kargs)


def goods_design_path(instance, filename):
    return f"goods/{instance.goods.entertainer}/{instance.goods.category}/{instance.goods.creator.username}/{filename}"


class Design(models.Model):
    goods = models.ForeignKey(Goods, on_delete=models.CASCADE, related_name="design")
    design = models.ImageField(upload_to=goods_design_path)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.goods}의 디자인"

    class Meta:
        ordering = ["-created_at"]
        indexes = [
            models.Index(fields=["goods"]),
            models.Index(fields=["created_at"]),
        ]

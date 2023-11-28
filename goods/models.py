from django.db import models

from account.models import User


class Entertainer(models.Model):
    name = models.CharField(max_length=25, unique=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=25, unique=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


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
    likes = models.ManyToManyField(
        User, related_name="like_goods", blank=True, null=True
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"[{self.entertainer}] {self.creator} 굿즈"


def goods_design_path(instance, filename):
    return f"goods/{instance.goods.entertainer}/{instance.goods.category}/{instance.goods.creator.username}/{filename}"


class Design(models.Model):
    goods = models.ForeignKey(Goods, on_delete=models.CASCADE, related_name="design")
    design = models.ImageField(upload_to=goods_design_path)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.goods}의 디자인"

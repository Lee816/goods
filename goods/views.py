from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View

from .models import Goods, Category, Entertainer, Design


class GoodsView(LoginRequiredMixin, View):
    def get(self, request):
        goods_list = Goods.objects.all()
        return render(request, "goods/goods_list.html", {"goods_list": goods_list})

    def post(self, request):
        pass

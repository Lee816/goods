from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View

from goods.models import Goods


class HomeView(LoginRequiredMixin, View):
    def get(self, request):
        goods_list = Goods.objects.all()
        return render(request, "goods/goods_list.html", {"goods_list": goods_list})

    def post(self, request):
        return render(request, "base/bad_request.html")

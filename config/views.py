from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.db.models import Q

from goods.models import Goods


class HomeView(View):
    def get(self, request):
        if request.user:
            goods_list = Goods.objects.all()
            return render(request, "base/home.html", {"goods_list": goods_list})
        else:
            return render(request, "base/home.html")

    def post(self, request):
        word = request.POST["word"]

        goods_list = Goods.objects.filter(
            Q(entertainer__name__icontains=word)
            | Q(category__name__icontains=word)
            | Q(creator__icontains=word)
            | Q(description__icontains=word)
        )

        return render(request, "base/home.html", {"goods_list": goods_list})

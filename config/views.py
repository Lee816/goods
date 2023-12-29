from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View

from goods.models import Goods


class HomeView(View):
    def get(self, request):
        if request.user:
            goods_list = Goods.objects.all()
            return render(request, "home.html", {"goods_list": goods_list})
        else:
            return render(request, "home.html")

    def post(self, request):
        return render(request, "base/bad_request.html")

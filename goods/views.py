from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.http.response import JsonResponse

from account.models import User

from .models import Goods, Category, Entertainer, Design, Comment, Recomment


class GoodsListView(View):
    def get(self, request):
        goods_list = Goods.objects.all().order_by("-updated_at")
        return render(request, "goods/goods_list.html", {"goods_list": goods_list})

    def post(self, request):
        return render(request, "base/bad_request.html")


class GoodsDetailView(View):
    def get(self, request, pk):
        goods = get_object_or_404(Goods, id=pk)
        return render(request, "goods/goods_detail.html", {"goods": goods})


class GoodsCreateView(LoginRequiredMixin, View):
    def get(self, request):
        category = Category.objects.all()
        entertainer = Entertainer.objects.all()
        return render(
            request,
            "goods/goods_create.html",
            {"category": category, "entertainer": entertainer},
        )

    def post(self, request):
        category = get_object_or_404(Category, id=request.POST["category"])
        entertainer = get_object_or_404(Entertainer, id=request.POST["entertainer"])
        description = request.POST["description"]
        design_list = request.FILES.getlist("design")

        goods = Goods.objects.create(
            category=category,
            entertainer=entertainer,
            creator=request.user,
            description=description,
        )
        goods.save()

        for design in design_list:
            new_design = Design.objects.create(goods=goods, design=design)
            new_design.save()

        return redirect("goods:goods_list")


class GoodsUpdateView(LoginRequiredMixin, View):
    def get(self, request, pk):
        category = Category.objects.all()
        entertainer = Entertainer.objects.all()
        goods = get_object_or_404(Goods, id=pk)
        return render(
            request,
            "goods/goods_create.html",
            {"category": category, "entertainer": entertainer, "goods": goods},
        )

    def post(self, request, pk):
        category = get_object_or_404(Category, id=request.POST["category"])
        entertainer = get_object_or_404(Entertainer, id=request.POST["entertainer"])
        description = request.POST["description"]

        goods = get_object_or_404(Goods, id=pk)
        goods.category = category
        goods.entertainer = entertainer
        goods.description = description
        goods.save()

        return redirect("goods:goods_list")


class GoodsDeleteView(LoginRequiredMixin, View):
    def post(self, request, pk):
        goods = get_object_or_404(Goods, id=pk)
        goods.delete()

        return redirect("goods:goods_list")


class GoodsLikeView(LoginRequiredMixin, View):
    def get(self, request, pk):
        goods = get_object_or_404(Goods, id=pk)

        if Goods.objects.filter(id=pk, likes=request.user).exists():
            goods.likes.remove(request.user)
            goods.save()
            return JsonResponse({"message": "like", "count": goods.like_count})
        else:
            goods.likes.add(request.user)
            goods.save()
            return JsonResponse({"message": "unlike", "count": goods.like_count})


class CommentCreateView(LoginRequiredMixin, View):
    def post(self, request, pk):
        goods = get_object_or_404(Goods, id=pk)

        comment = Comment.objects.create(
            goods=goods, creator=request.user, content=request.POST["content"]
        )
        comment.save()

        return redirect("goods:goods_list")


class RecommentCreateView(LoginRequiredMixin, View):
    def post(self, request, pk):
        comment = get_object_or_404(Comment, id=pk)

        recomment = Recomment.objects.create(
            comment=comment, creator=request.user, content=request.POST["content"]
        )
        recomment.save()

        return redirect("goods:goods_list")

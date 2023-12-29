from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404

from account.models import User
from .models import Goods, Comment, Recomment


class Goods_Creator_Permission(LoginRequiredMixin):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return self.handle_no_permission()

        goods_id = self.kwargs["pk"]
        goods = get_object_or_404(Goods, id=goods_id)

        if goods.creator != request.user:
            return self.handle_no_permission()

        return super().dispatch(request, *args, **kwargs)


class Comment_Creator_Permission(LoginRequiredMixin):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return self.handle_no_permission()

        comment_id = self.kwargs["pk"]
        comment = get_object_or_404(Comment, id=comment_id)

        if comment.creator != request.user:
            return self.handle_no_permission()

        return super().dispatch(request, *args, **kwargs)


class Recomment_Creator_Permission(LoginRequiredMixin):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return self.handle_no_permission()

        recomment_id = self.kwargs["pk"]
        recomment = get_object_or_404(Comment, id=recomment_id)

        if recomment.creator != request.user:
            return self.handle_no_permission()

        return super().dispatch(request, *args, **kwargs)

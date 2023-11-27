from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404

from .models import User


class User_Update_Permission(LoginRequiredMixin):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return self.handle_no_permission()

        user_id = self.kwargs["pk"]
        user = get_object_or_404(User, id=user_id)

        if user != request.user:
            return self.handle_no_permission()

        return super().dispatch(request, *args, **kwargs)

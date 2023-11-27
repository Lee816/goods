from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import User
from .permissions import User_Update_Permission


class RegisterView(View):
    def get(self, request):
        return render(request, "account/register.html")

    def post(self, request):
        username = request.POST["username"]
        nickname = request.POST["nickname"]
        email = request.POST["email"]
        phone = request.POST["phone"]

        new_user = User.objects.create(
            username=username, nickname=nickname, email=email, phone=phone
        )
        new_user.set_password(request.POST["password"])
        new_user.save()

        return redirect("home")


class LoginView(View):
    def get(self, request):
        return render(request, "account/login.html")

    def post(self, request):
        email = request.POST["email"]
        password = request.POST["password"]

        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            return redirect("home")

        return render(request, "base/bad_request.html")


class LogoutView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, "base/bad_request.html")

    def post(self, request):
        logout(request)
        return redirect("account:login")


class UpdateView(User_Update_Permission, View):
    def get(self, request, pk):
        user = get_object_or_404(User, id=pk)

        if user == request.user:
            return render(request, "account/update.html")

    def post(self, request, pk):
        user = get_object_or_404(User, id=pk)

        user.nickname = request.POST["nickname"]
        user.phone = request.POST["phone"]
        user.introduce = request.POST["introduce"]
        user.user_image = request.FILES["user_image"]

        user.save()

        return redirect("home")

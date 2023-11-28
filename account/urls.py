from django.urls import path

from . import views

app_name = "account"
urlpatterns = [
    path("register/", views.RegisterView.as_view(), name="register"),
    path("login/", views.LoginView.as_view(), name="login"),
    path("logout/", views.LogoutView.as_view(), name="logout"),
    path("update/<int:pk>/", views.UpdateView.as_view(), name="update"),
    path("pwupdate/<int:pk>/", views.PWUpdateView.as_view(), name="pw_update"),
    path("pwreset/<int:pk>/", views.PWResetView.as_view(), name="pw_reset"),
    path("pw_confirm/<int:pk>/", views.PWResetConfirmView.as_view(), name="pw_confirm"),
]

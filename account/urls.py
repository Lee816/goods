from django.urls import path

from . import views

app_name = "account"
urlpatterns = [
    path("<int:pk>/", views.UserView.as_view(), name="main"),
    path("register/", views.RegisterView.as_view(), name="register"),
    path("login/", views.LoginView.as_view(), name="login"),
    path("logout/", views.LogoutView.as_view(), name="logout"),
    path("update/<int:pk>/", views.UpdateView.as_view(), name="update"),
    path("pwupdate/<int:pk>/", views.PWUpdateView.as_view(), name="pw_update"),
    path("pwreset/", views.PWResetView.as_view(), name="pw_reset"),
    path("pw_confirm/<int:pk>/", views.PWResetConfirmView.as_view(), name="pw_confirm"),
]

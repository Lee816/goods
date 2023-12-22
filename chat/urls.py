from django.urls import path

from . import views

app_name = "chat"
urlpatterns = [
    path("<int:pk>/room/", views.RoomView.as_view(), name="room"),
]

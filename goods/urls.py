from django.urls import path

from . import views

app_name = "goods"
urlpatterns = [
    path("", views.GoodsListView.as_view(), name="goods_list"),
    path("create/", views.GoodsCreateView.as_view(), name="goods_create"),
    path("update/<int:pk>/", views.GoodsUpdateView.as_view(), name="goods_update"),
]

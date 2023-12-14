from django.urls import path

from . import views

app_name = "goods"
urlpatterns = [
    path("", views.GoodsListView.as_view(), name="goods_list"),
    path("create/", views.GoodsCreateView.as_view(), name="goods_create"),
    path("<int:pk>/update/", views.GoodsUpdateView.as_view(), name="goods_update"),
    path("<int:pk>/delete/", views.GoodsDeleteView.as_view(), name="goods_delete"),
    path("<int:pk>/like/", views.GoodsLikeView.as_view(), name="goods_like"),
]

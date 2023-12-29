from django.urls import path

from . import views

app_name = "goods"
urlpatterns = [
    path("<int:pk>/", views.GoodsDetailView.as_view(), name="goods_detail"),
    path("create/", views.GoodsCreateView.as_view(), name="goods_create"),
    path("<int:pk>/update/", views.GoodsUpdateView.as_view(), name="goods_update"),
    path("<int:pk>/delete/", views.GoodsDeleteView.as_view(), name="goods_delete"),
    path("<int:pk>/like/", views.GoodsLikeView.as_view(), name="goods_like"),
    path(
        "<int:pk>/comment/create/",
        views.CommentCreateView.as_view(),
        name="comment_create",
    ),
    path(
        "comment/<int:pk>/update/",
        views.CommentUpdateView.as_view(),
        name="comment_update",
    ),
    path(
        "comment/<int:pk>/delete/",
        views.CommentDeleteView.as_view(),
        name="comment_delete",
    ),
    path(
        "comment/<int:pk>/recomment/create/",
        views.RecommentCreateView.as_view(),
        name="recomment_create",
    ),
    path(
        "comment/recomment/<int:pk>/update/",
        views.RecommentUpdateView.as_view(),
        name="recomment_update",
    ),
    path(
        "comment/recomment/<int:pk>/delete/",
        views.RecommentDeleteView.as_view(),
        name="recomment_delete",
    ),
]

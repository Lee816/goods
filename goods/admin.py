from django.contrib import admin

from .models import Category, Entertainer, Goods, Design, Comment, Recomment


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name"]
    list_filter = ["created_at", "name"]
    search_fields = ["name"]
    ordering = ["-created_at"]


@admin.register(Entertainer)
class EntertainerAdmin(admin.ModelAdmin):
    list_display = ["name"]
    list_filter = ["created_at", "name"]
    search_fields = ["name"]
    ordering = ["-created_at"]


class DesignAdmin(admin.TabularInline):
    model = Design


class RecommentAdmin(admin.TabularInline):
    model = Recomment


admin.site.register(Design)
admin.site.register(Recomment)


@admin.register(Goods)
class GoodsAdmin(admin.ModelAdmin):
    list_display = ["entertainer", "category", "creator", "created_at"]
    list_filter = ["created_at", "entertainer", "category", "creator"]
    search_fields = ["entertainer", "category", "creator", "description"]
    ordering = ["-created_at"]
    inlines = [
        DesignAdmin,
    ]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ["goods", "creator", "created_at"]
    list_filter = ["created_at", "goods", "creator"]
    search_fields = ["goods", "content", "creator"]
    ordering = ["-created_at"]
    inlines = [
        RecommentAdmin,
    ]

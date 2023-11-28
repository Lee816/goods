from django.contrib import admin

from .models import Category, Entertainer, Goods, Design


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


admin.site.register(Design)


@admin.register(Goods)
class GoodsAdmin(admin.ModelAdmin):
    list_display = ["entertainer", "category", "creator", "created_at"]
    list_filter = ["created_at", "entertainer", "category", "creator"]
    search_fields = ["entertainer", "category", "creator", "description"]
    ordering = ["-created_at"]
    inlines = [
        DesignAdmin,
    ]

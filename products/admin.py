from django.contrib import admin
from .models import Product, Category, Style

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'rating',
        'image',
    )

    ordering = ('sku',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )

class MusicStyleAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


class CelebrityAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'comment',
        'image',
        'friendly_name',
        'product',
    )

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Style, MusicStyleAdmin)
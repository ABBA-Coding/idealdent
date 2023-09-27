from django.contrib import admin
from api.products import models


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    ...


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    ...


@admin.register(models.SubCategory)
class SubcategoryAdmin(admin.ModelAdmin):
    ...

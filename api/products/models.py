from django.db import models
from django.utils.translation import gettext_lazy as _


class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = _('Категория')
        verbose_name_plural = _('Категории')

    def __str__(self):
        return self.name


class SubCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    image = models.ImageField(null=True, blank=True, upload_to='subcategories')

    class Meta:
        verbose_name = _('Субкатегория')
        verbose_name_plural = _('Субкатегории')

    def __str__(self):
        return f"Category: {self.category.name} | Subcategory: {self.name}"


class Product(models.Model):
    class CurrencyChoices(models.TextChoices):
        USD = "$", "$"
        UZS = "so'm", "so'm"

    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    image = models.ImageField(null=True, blank=True, upload_to="products")
    code = models.CharField(max_length=10)
    artikul = models.CharField(max_length=12)
    unit = models.CharField("Единица измерения", max_length=10, null=True, blank=True)
    cost = models.IntegerField("Цена")
    cost_currency = models.CharField(max_length=4, choices=CurrencyChoices.choices, default=CurrencyChoices.USD)
    external_code = models.CharField(max_length=50)
    country = models.CharField(max_length=20)

    class Meta:
        verbose_name = _('Продукт')
        verbose_name_plural = _('Продукты')

    def __str__(self):
        return self.name

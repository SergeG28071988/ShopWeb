from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название товара", null=True, blank=True)
    description = models.TextField(verbose_name="Описание товара", null=True, blank=True)
    quantity = models.IntegerField(verbose_name="Количество товара", null=True, blank=True)
    price = models.DecimalField(max_digits=10, verbose_name="Цена товара", decimal_places=2, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
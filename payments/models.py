from django.db import models
from django.core import validators


class Item(models.Model):
    name = models.CharField(max_length=250, verbose_name="Наименование товара")
    description = models.TextField(max_length=5000, blank=True, verbose_name="Описание")
    price = models.IntegerField(
        verbose_name="Цена",
        validators=[
            validators.MinValueValidator(50),
            validators.MaxValueValidator(10000000),
        ],
    )

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"

    def convert_to_usd(self):
        return "{0:.2f}".format(self.price / 100)

    def __str__(self):
        return self.name

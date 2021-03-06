from django.db import models
from django.core.validators import MinValueValidator
from django.urls import reverse


class Product(models.Model):
    """ Товар для магазина. """
    name = models.CharField(
        max_length=50,
        unique=True,    # названия товаров не должны повторяться
    )
    description = models.TextField()
    quantity = models.IntegerField(
        validators=[MinValueValidator(0)],
    )
    # поле категории будет ссылаться на модель категории
    category = models.ForeignKey(
        to='Category',
        on_delete=models.CASCADE,
        related_name='products',    # все продукты в категории будут доступны через поле products
    )
    price = models.FloatField(
        validators=[MinValueValidator(0.0)],
    )

    def __str__(self):
        return f'{self.name.title()}: {self.description[:20]}'

    def get_absolute_url(self):
        """ Вернуть url, зарегистрированный для отображения одиночного товара """
        return reverse('product_detail', args=[str(self.id)])


class Category(models.Model):
    """ Категория, к которой будет привязываться товар. """
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name.title()

from django.conf import settings
from django.db import models


class Ad(models.Model):
    title = models.CharField(
        max_length=200,
        verbose_name="Наименование товара",
        help_text="Введите наименование товара",
    )

    price = models.PositiveIntegerField(
        verbose_name="Цена товара",
        help_text="Укажите цену товара",
    )
    description = models.CharField(
        max_length=1000,
        null=True,
        blank=True,
        verbose_name="Описание товара",
        help_text="Опишите подробней ваш товар",
    )

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="ads",
        verbose_name="Автор объявления",
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Время создания объявления"
    )

    image = models.ImageField(
        upload_to='ads/%Y/%m',
        null=True,
        blank=True,
        verbose_name="Фото",
        help_text="Фото для  вашего объявления",
    )

    class Meta:
        ordering = ('-created_at',)
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'


class Comment(models.Model):
    text = models.CharField(
        max_length=2000,
        verbose_name="Комментарий",
        help_text="Напишите свой комментарий",
    )

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="comments",
        verbose_name="Автор комментария",
    )

    ad = models.ForeignKey(
        Ad,
        on_delete=models.CASCADE,
        related_name="comments",
        verbose_name="Объявление",
        help_text="Объявление, к которому относится этот комментарий"
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Время создания  комментария",
    )

    class Meta:
        ordering = ('-created_at',)
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

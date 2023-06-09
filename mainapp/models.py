from django.db import models
from authapp.models import CustomUser
from django.utils.translation import gettext_lazy as _
from django.utils import timezone


class GoodsManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(deleted=False)


class Category(models.Model):
    name = models.CharField(max_length=300)

    def __str__(self):
        return self.name


class Product(models.Model):
    objects = GoodsManager()
    title = models.CharField(max_length=300, verbose_name='Заголовок')
    description = models.TextField(verbose_name='Описание')
    cost = models.DecimalField(
        max_digits=8, decimal_places=2, verbose_name='Стоимость', default=0)
    quantity = models.IntegerField(default=1, verbose_name='Количество')
    image = models.ImageField(upload_to='products/',
                              default='products/default_product.png')
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name='Создано')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Обновлено')
    deleted = models.BooleanField(default=False, verbose_name='Удалено')
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, default=6)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'

    def delete(self, *args, **kwargs):
        self.deleted = True
        self.save()


class BasketItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1, max_length=6)


class Comment(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    post = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=True)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text

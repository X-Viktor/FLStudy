from django.db import models

from users.models import User


class Category(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название')
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['title']

    def __str__(self):
        return self.title


class Task(models.Model):
    STATUS_CHOICES = (
        (1, 'Открыто'),
        (2, 'Выполняется'),
        (3, 'Закрыто'),
    )

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='tasks',
        verbose_name='Категория'
    )
    title = models.CharField(max_length=150, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    reward = models.DecimalField(
        max_digits=9,
        decimal_places=2,
        verbose_name='Вознаграждение'
    )
    status = models.PositiveSmallIntegerField(
        choices=STATUS_CHOICES,
        default=1,
        verbose_name='Статус'
    )
    customer = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='tasks_created',
        verbose_name='Заказчик'
    )
    performer = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        related_name='tasks_taken',
        blank=True,
        null=True,
        verbose_name='Исполнитель'
    )
    date_creation = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата публикации'
    )

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
        ordering = ['-date_creation']

    def __str__(self):
        return self.title

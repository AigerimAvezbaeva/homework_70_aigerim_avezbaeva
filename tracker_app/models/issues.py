from django.db import models
from django.utils import timezone

class Issue(models.Model):
    summary = models.CharField(
        max_length=200,
        null=False,
        blank=True,
        default="Задача",
        verbose_name="Заголовок")
    description = models.TextField(
        max_length=3000,
        null=False,
        blank=True,
        verbose_name="Описание")
    status = models.ForeignKey(
        to='tracker_app.Status',
        related_name='issues',
        verbose_name='Статус',
        blank=False,
        null=True,
        on_delete=models.PROTECT
    )
    type = models.ManyToManyField(
        to='tracker_app.Type',
        related_name='issues',
        verbose_name='Тип'
    )
    project = models.ForeignKey(
        to='tracker_app.Project',
        related_name='issues',
        verbose_name='Проект',
        on_delete=models.PROTECT
    )
    created_at = models.DateField(
        auto_now_add=True,
        verbose_name="Время создания")
    updated_at = models.DateField(
        auto_now=True,
        verbose_name="Дата и время обновления")

    is_deleted = models.BooleanField(
        verbose_name='Удалено',
        null=False,
        default=False
    )
    deleted_at = models.DateTimeField(
        verbose_name='Дата и время удаления',
        null=True,
        blank=True,
        default=None)

    def delete(self, using=None, keep_parents=False):
        self.is_deleted = True
        self.deleted_at = timezone.now()
        self.save()

from django.db import models


class Task(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, null=False, blank=False, editable=True, verbose_name='Дата создания')
    description = models.TextField(null=False, blank=False, editable=True, verbose_name='Описание задачи')

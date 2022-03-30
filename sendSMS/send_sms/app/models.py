from django.db import models


# Create your models here.

class Send(models.Model):
    recipient = models.CharField(verbose_name='Номер телефона', max_length=20)
    message_id = models.CharField(verbose_name='СМС ID', max_length=200)
    text = models.TextField(verbose_name='Текст')
    status = models.CharField(verbose_name="Статус отправки", max_length=10)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    def str(self):
        return self.recipient


class User(models.Model):
    full_name = models.CharField(verbose_name='имя абонента', max_length=20)
    user_number = models.CharField(verbose_name='Номер телефона', max_length=20)
    message_id = models.CharField(verbose_name='СМС ID', max_length=200)
    text = models.TextField(verbose_name='Текст')

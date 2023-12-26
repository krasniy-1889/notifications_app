import pytz
from django.db import models


class Client(models.Model):
    """Модель контакта"""

    TIMEZONES = tuple(zip(pytz.all_timezones, pytz.all_timezones))

    phone_number = models.CharField(
        max_length=15,
        help_text="номер телефона клиента в формате 7XXXXXXXXXX (X - цифра от 0 до 9)",
    )
    mobile_code = models.CharField(max_length=10)
    tag = models.CharField(null=True, blank=False, max_length=50)
    time_zone = models.CharField(max_length=32, choices=TIMEZONES, default="UTC")

    class Meta:
        verbose_name = "Mailing"
        verbose_name_plural = "Mailings"


class Mailing(models.Model):
    """Модель рассылки"""

    text = models.TextField()
    tag = models.CharField(max_length=50)
    code = models.CharField(max_length=50)
    start_send_time = models.DateTimeField()
    end_send_time = models.DateTimeField()

    class Meta:
        verbose_name = "Client"
        verbose_name_plural = "Clients"


class Message(models.Model):
    """Модель сообщения"""

    class STATUS_CHOICES(models.TextChoices):
        SEND = "S", "send"
        NOT_SEND = "S", "not send"

    send_time = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES.choices)
    mailing = models.ForeignKey(
        Mailing, on_delete=models.CASCADE, related_name="messages"
    )
    client = models.ForeignKey(
        Client, on_delete=models.CASCADE, related_name="messages"
    )

    class Meta:
        verbose_name = "Message"
        verbose_name_plural = "Messages"

from django.core.mail import send_mail
from django.db import models
from Vishnya.settings import EMAIL_HOST_USER
from structure.models import Basket
from users.models import User


class Order(models.Model):
    STATUS_CHOICES = [(0, "Создаётся"), (1, "Оплачен"), (2, "Доставлен")]
    status = models.IntegerField(choices=STATUS_CHOICES, default=0)
    date = models.DateField().auto_now
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.TextField(default='Россия, Москва, ул. Мира, дом 666')
    basket_history = models.JSONField(default=dict)
    payment_id = models.CharField(max_length=255, null=True, blank=True)
    payment_method_id = models.CharField(max_length=255, null=True, blank=True)
    is_active = models.BooleanField(default=False)
    send_mail_flag = models.BooleanField(default=False)

    def __str__(self):
        return f'Order #{self.id}'

    def update_after_payment(self, payment_id):
        baskets = Basket.objects.filter(user=self.user)
        self.status = 1
        self.basket_history = {
            'purchased_items': [basket.de_json() for basket in baskets],
            'total_sum': baskets.total_sum()
        }
        self.payment_id = payment_id
        baskets.delete()
        self.save()

    def send_mail(self, receipt):
        message = f"Номер чека: {receipt['id']} \nТип: {receipt['type']} \nID платежа: {receipt['payment_id']} \nСтатус: {receipt['status']} \nНомер фискального документа: {receipt['fiscal_document_number']} \nНомер фискального накопителя: {receipt['fiscal_storage_number']} \nФискальный признак: {receipt['fiscal_attribute']} \nДата и время регистрации: {receipt['registered_at']} \nID чека в облачной кассе: {receipt['fiscal_provider_id']}\n ПРОДУКТЫ: \n"
        if self.is_active:
            message += f"\n Подписка, 150 руб./мес. \n Первый платёж - 50 руб."
        else:
            for item in receipt['items']:
                message += f"\n {item['description']}      Цена: { item['amount']['value'] } { item['amount']['currency'] }      Количество: {item['quantity']}"
            message += f"\n \n Общая стоимость заказа: {self.basket_history['total_sum']} руб."
        send_mail(
            f"Ваш чек по заказу {self.pk}",
            message,
            EMAIL_HOST_USER,
            [self.user.email],
        )
        self.send_mail_flag = True
        self.save()
